#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抖音爆款脚本改写器 v2 —— 国内热搜优先，Horizon日报补充"""
import os, sys, json, glob, io
from datetime import datetime
from openai import OpenAI

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

SYSTEM = """你是抖音百万粉科技博主，人设是"帮你搞懂AI的邻居大哥"。你的脚本风格：
- 不念新闻，讲观点。每条视频都有一个明确的"态度"
- 像在饭桌上跟朋友聊天，不是播报
- 用类比和场景让小白也能听懂
- 自信、有主见、偶尔犀利"""

PROMPT = """从下面两份素材里，挑出最值得做的**2条**选题，写成抖音口播脚本。

素材1是国内实时热搜（优先用这个，更接地气），素材2是AI行业日报（作补充）。

══════════════════
【选题铁律】
══════════════════

不做：纯海外话题、纯技术细节、没有冲突点的
优先：影响普通人生活的（微信/AI替代/隐私）、有争议的、国产AI突破、大厂打架

══════════════════
【脚本结构】
══════════════════

钩子（0-3秒）：具体场景/身份代入/反直觉数据，不用"你敢信吗""炸裂了"
发生了什么（5秒）：谁+干了什么+影响，必须用类比
为什么重要（10-20秒）：你的洞察和态度，不能骑墙
结尾（3秒）：个人态度收尾，"反正我已经...""留给xx的时间不多了"

══════════════════
【输出格式】只要2条
══════════════════

## 今日脚本

### 脚本1 | [标题要有态度]
> 为什么选这条：[一句话]
> 画面：[3-5个画面用 -> 连接]
> 口播：
[90-130字，口语化，有态度]

### 脚本2 | [标题要有态度]
> 为什么选这条：[一句话]
> 画面：[3-5个画面用 -> 连接]
> 口播：
[90-130字，口语化，有态度]

══════════════════
【素材1：国内实时热搜】
══════════════════

"""

def find_file(docs_dir, pattern):
    files = sorted(glob.glob(os.path.join(docs_dir, "_posts", pattern)), reverse=True)
    return files[0] if files else None

def read_file(filepath):
    if not filepath: return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def call_deepseek(china_hot, horizon_summary):
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    user = PROMPT + (china_hot or "(no China hot data)") + "\n\n---\n【素材2：AI行业日报】\n---\n\n" + (horizon_summary or "(no daily data)")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.85, max_tokens=2500,
    )
    return response.choices[0].message.content

def save_scripts(docs_dir, scripts):
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(docs_dir, "_posts", f"{today}-douyin-scripts.md")
    full = f"---\nlayout: default\ntitle: \"Douyin Scripts - {today}\"\ndate: {today}\nlang: zh\ndouyin: true\n---\n\n{scripts}\n\n---\n> DeepSeek | [Daily Report](/ai-tech-daily/) | Review before recording\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full)
    print(f"[OK] Saved: {filepath}")

def main():
    if not DEEPSEEK_API_KEY:
        print("[FAIL] DEEPSEEK_API_KEY not set"); sys.exit(1)
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
    china_path = find_file(docs_dir, "*-china-hot.md")
    horizon_path = find_file(docs_dir, "*-summary-zh.md")
    china = read_file(china_path)
    horizon = read_file(horizon_path)
    print(f"China hot: {'YES ' + str(len(china)) + 'chars' if china else 'NO'}")
    print(f"Horizon: {'YES ' + str(len(horizon)) + 'chars' if horizon else 'NO'}")
    if not china and not horizon:
        print("[SKIP] No data"); sys.exit(0)
    print("DeepSeek rewriting...")
    scripts = call_deepseek(china, horizon)
    save_scripts(docs_dir, scripts)
    print("=" * 50)
    print(scripts[:600] + ("..." if len(scripts) > 600 else ""))

if __name__ == "__main__":
    main()
