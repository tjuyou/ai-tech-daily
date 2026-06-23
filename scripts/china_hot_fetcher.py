#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""国内热搜抓取器 v2 —— 多源容错，海外可用"""
import os, sys, json, io
from datetime import datetime
import urllib.request

# Windows 控制台 UTF-8 修复
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_ENDPOINTS = [
    "https://api-hot.imsyy.top",
    "https://hot-api.imsyy.top",
]

KEYWORDS = ["AI", "人工智能", "科技", "GPT", "大模型", "机器人", "DeepSeek", 
            "OpenAI", "苹果", "华为", "特斯拉", "小米", "芯片", "微信", 
            "抖音", "互联网", "马斯克", "自动驾驶", "手机", "Claude",
            "Gemini", "Copilot", "Sora", "Agent", "开源", "编程"]

PLATFORMS = ["weibo", "zhihu", "baidu", "douyin", "toutiao", "36kr", "ithome"]
PLATFORM_NAMES = {
    "weibo": "微博热搜", "zhihu": "知乎热榜", "baidu": "百度热搜",
    "douyin": "抖音热点", "toutiao": "今日头条", "36kr": "36氪热榜", "ithome": "IT之家"
}

def find_working_api():
    for api in API_ENDPOINTS:
        try:
            url = f"{api}/weibo"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode())
                if data.get("data"):
                    print(f"[OK] API: {api}")
                    return api
        except Exception as e:
            print(f"[SKIP] {api}: {e}")
    return None

def fetch_platform(api_base, platform):
    url = f"{api_base}/{platform}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        return data.get("data", [])
    except Exception as e:
        print(f"  [FAIL] {platform}: {e}")
        return []

def match_keywords(title):
    title_lower = title.lower()
    return any(kw.lower() in title_lower for kw in KEYWORDS)

def fetch_all(api_base):
    all_items = []
    for platform in PLATFORMS:
        name = PLATFORM_NAMES[platform]
        print(f"  {name}...", end=" ")
        items = fetch_platform(api_base, platform)
        filtered = [item for item in items if match_keywords(
            item.get("title", "") + item.get("desc", "")
        )]
        print(f"{len(items)} total -> {len(filtered)} AI-related")
        for item in filtered[:6]:
            all_items.append({
                "platform": name,
                "title": item.get("title", ""),
                "desc": item.get("desc", ""),
                "hot": item.get("hot", ""),
                "url": item.get("url", ""),
            })
    return all_items

def save_markdown(items, docs_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(docs_dir, "_posts", f"{today}-china-hot.md")
    platforms = {}
    for item in items:
        platforms.setdefault(item["platform"], []).append(item)
    
    lines = [
        "---",
        "layout: default",
        f"title: \"China Tech Hot - {today}\"",
        f"date: {today}", "lang: zh",
        "---",
        f"# China Tech Hot Topics - {today}",
        f"> Weibo/Zhihu/Baidu/Douyin/Toutiao/36kr/ITHome | {len(items)} AI/tech items\n",
    ]
    for pname, pitems in platforms.items():
        lines.append(f"## {pname}\n")
        for i, item in enumerate(pitems[:5], 1):
            hot = f" [{item['hot']}]" if item.get("hot") else ""
            lines.append(f"{i}. **{item['title']}**{hot}")
            if item.get("desc"):
                lines.append(f"   > {item['desc'][:120]}")
            lines.append("")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n[OK] Saved: {filepath}")
    return filepath

def main():
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
    os.makedirs(os.path.join(docs_dir, "_posts"), exist_ok=True)
    
    print("=" * 50)
    print("China Hot Topics Fetcher v2")
    print("=" * 50)
    
    api = find_working_api()
    if not api:
        print("[FAIL] All API endpoints unreachable")
        today = datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(docs_dir, "_posts", f"{today}-china-hot.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\nlayout: default\ntitle: \"China Hot - {today}\"\ndate: {today}\n---\n\n> API unreachable\n")
        sys.exit(0)
    
    items = fetch_all(api)
    print(f"\nTotal: {len(items)} AI/tech hot items\n")
    
    if items:
        save_markdown(items, docs_dir)
        print("TOP 10:")
        for i, item in enumerate(items[:10], 1):
            hot = f" [{item['hot']}]" if item.get("hot") else ""
            print(f"  {i}. [{item['platform']}]{hot} {item['title'][:60]}")
    else:
        print("No AI-related hot topics found today")

if __name__ == "__main__":
    main()
