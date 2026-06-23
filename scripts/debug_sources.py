import urllib.request, ssl, json, re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0'}

print("=== BAIDU ===")
try:
    req = urllib.request.Request('https://top.baidu.com/board?tab=realtime', headers=h)
    html = urllib.request.urlopen(req, timeout=10, context=ctx).read().decode()
    m = re.search(r'<!--s-data:(.*?)-->', html, re.DOTALL)
    if m:
        data = json.loads(m.group(1))
        cards = data['data']['cards']
        for card in cards[:1]:
            for c in card['content'][:3]:
                print(f"  {c.get('word','')} | {c.get('hotScore','')}")
    else:
        print(f"  no s-data, html len={len(html)}")
except Exception as e:
    print(f"  ERROR: {e}")

print("=== WEIBO ===")
try:
    req = urllib.request.Request('https://s.weibo.com/top/summary?cate=realtimehot', headers=h)
    html = urllib.request.urlopen(req, timeout=10, context=ctx).read().decode()
    matches = re.findall(r'td-02.*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
    print(f"  {len(matches)} matches")
    for m in matches[:5]:
        print(f"  {re.sub(r'<[^>]+>','',m).strip()[:50]}")
except Exception as e:
    print(f"  ERROR: {e}")

print("=== ZHIHU ===")
try:
    req = urllib.request.Request('https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=5', headers=h)
    data = json.loads(urllib.request.urlopen(req, timeout=10, context=ctx).read().decode())
    for item in data.get('data', [])[:3]:
        print(f"  {item.get('target',{}).get('title','')[:50]}")
except Exception as e:
    print(f"  ERROR: {e}")

print("=== 36KR ===")
try:
    req = urllib.request.Request('https://www.36kr.com/hot-list/hotflash?b_id=hotflash&per_page=5', headers=h)
    data = json.loads(urllib.request.urlopen(req, timeout=10, context=ctx).read().decode())
    for item in data.get('data',{}).get('items',[])[:3]:
        print(f"  {item.get('title','')[:50]}")
except Exception as e:
    print(f"  ERROR: {e}")
