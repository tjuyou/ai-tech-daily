#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""国内热搜抓取器 v5 —— 只抓验证过的源，稳"""
import os, sys, json, io, ssl, re, gzip
from datetime import datetime
import urllib.request

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

KEYWORDS = ["AI", "人工智能", "科技", "GPT", "大模型", "机器人", "DeepSeek", 
            "OpenAI", "苹果", "华为", "特斯拉", "小米", "芯片", "微信", 
            "抖音", "马斯克", "自动驾驶", "手机", "Claude", "开源", "编程",
            "量子", "航天", "卫星", "新能源", "Manus", "Sora", "Gemini",
            "Agent", "Copilot", "京东", "阿里", "腾讯", "英伟达", "微软",
            "谷歌", "字节", "快手", "美团", "互联网", "电商"]

H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def fetch_raw(url):
    try:
        req = urllib.request.Request(url, headers=H)
        with urllib.request.urlopen(req, timeout=12, context=ssl_ctx) as resp:
            raw = resp.read()
        if resp.headers.get('Content-Encoding') == 'gzip':
            raw = gzip.decompress(raw)
        for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030', 'latin-1']:
            try: return raw.decode(enc)
            except: continue
        return raw.decode('utf-8', errors='replace')
    except: return None

def parse_baidu():
    """百度热搜 - 稳定"""
    html = fetch_raw("https://top.baidu.com/board?tab=realtime")
    if not html: return []
    items = []
    try:
        m = re.search(r'<!--s-data:(.*?)-->', html, re.DOTALL)
        if m:
            data = json.loads(m.group(1))
            for card in data.get("data", {}).get("cards", []):
                for c in card.get("content", []):
                    t = c.get("word") or c.get("query", "")
                    if t and len(t) > 1:
                        items.append({"title": t, "hot": str(c.get("hotScore","")), "url": c.get("url","")})
    except: pass
    return items

def parse_weibo():
    """微博热搜 - 直接扒热搜页"""
    html = fetch_raw("https://s.weibo.com/top/summary?cate=realtimehot")
    if not html: return []
    items = []
    try:
        for m in re.finditer(r'<td class="td-02">.*?<a[^>]*>(.*?)</a>.*?<span>(\d+)</span>', html, re.DOTALL):
            title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            hot = m.group(2)
            if title: items.append({"title": title, "hot": hot, "url": ""})
    except: pass
    return items

def parse_zhihu():
    """知乎热榜 - API"""
    html = fetch_raw("https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true")
    if not html: return []
    items = []
    try:
        data = json.loads(html)
        for item in data.get("data", []):
            t = item.get("target", {})
            title = t.get("title", "")
            if title:
                items.append({"title": title, "desc": (t.get("excerpt","") or "")[:100],
                             "hot": str(t.get("answer_count","")), "url": t.get("url","")})
    except: pass
    return items

def match(title):
    return any(kw.lower() in title.lower() for kw in KEYWORDS)

def save(items, docs_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(docs_dir, "_posts", f"{today}-china-hot.md")
    plats = {}
    for it in items: plats.setdefault(it["platform"], []).append(it)
    
    lines = ["---", "layout: default", f"title: \"China Tech Hot - {today}\"",
             f"date: {today}", "lang: zh", "---",
             f"# China Tech Hot - {today}",
             f"> Baidu/Weibo/Zhihu | {len(items)} AI/tech items\n"]
    for pn, pitems in plats.items():
        lines.append(f"## {pn}\n")
        for i, it in enumerate(pitems[:5], 1):
            h = f" [{it.get('hot','')}]" if it.get("hot") else ""
            lines.append(f"{i}. **{it['title']}**{h}")
            if it.get("desc"): lines.append(f"   > {it['desc'][:120]}")
            lines.append("")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n[OK] {filepath}")

SOURCES = [
    ("baidu", "百度热搜", parse_baidu),
    ("weibo", "微博热搜", parse_weibo),
    ("zhihu", "知乎热榜", parse_zhihu),
]

def main():
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
    os.makedirs(os.path.join(docs_dir, "_posts"), exist_ok=True)
    
    print("=" * 50)
    print("China Hot Fetcher v5")
    print("=" * 50)
    
    all_items = []
    for key, name, func in SOURCES:
        print(f"  {name}...", end=" ", flush=True)
        raw = func()
        if not raw:
            print("FAIL"); continue
        filtered = [it for it in raw if match(it["title"])]
        print(f"{len(raw)} total -> {len(filtered)} AI")
        for it in filtered[:6]:
            it["platform"] = name
            all_items.append(it)
    
    print(f"\nTotal: {len(all_items)} AI/tech items\n")
    if all_items:
        save(all_items, docs_dir)
        for i, it in enumerate(all_items[:15], 1):
            h = f" [{it.get('hot','')}]" if it.get("hot") else ""
            print(f"  {i}. [{it['platform']}]{h} {it['title'][:60]}")
    else:
        print("No AI/tech hot topics today - 正常，科技不是每天都有热搜")
        today = datetime.now().strftime("%Y-%m-%d")
        with open(os.path.join(docs_dir, "_posts", f"{today}-china-hot.md"), "w", encoding="utf-8") as f:
            f.write(f"---\nlayout: default\ntitle: \"China Hot - {today}\"\ndate: {today}\n---\n\n> No AI tech hot items today\n")

if __name__ == "__main__":
    main()
