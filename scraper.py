import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celebrity_mission():
    # المصدر الذي طلبته: مشاهير العرب (قسم أخبار المشاهير)
    rss_url = "https://celebritiesarab.com/?feed=rss2&cat=27"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الإعلاني الخاص بك
        my_ad_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"✨ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:30]):
            title = item.title.text
            
            # محرك استخراج الصور المخصص لموقع celebritiesarab
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            if not img_url:
                content = item.find('content:encoded') or item.description
                if content:
                    img_match = re.search(r'src="(.*?)"', str(content))
                    if img_match:
                        img_url = img_match.group(1)
            
            if not img_url:
                img_url = "https://celebritiesarab.com/wp-content/uploads/2023/logo.png"

            news_html += f'''
            <article class="celeb-card">
                <div class="trending-badge">تريند</div>
                <div class="img-wrapper">
                    <a href="{my_ad_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Celebrity News">
                    </a>
                </div>
                <div class="card-content">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>🎬 أخبار المشاهير</span>
                        <span>⏱️ {datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <a href="{my_ad_link}" target="_blank" class="btn-primary">شاهد التفاصيل والصور ⚡</a>
                </div>
            </article>'''

            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="vip-ad-box">
                    <a href="{my_ad_link}" target="_blank">
                        <div class="ad-inner">
                            <span class="exclusive">حصري VIP</span>
                            <h3>تسريب فيديو يثير الجدل للفنانة المشهورة!</h3>
                            <p>اضغط هنا لمشاهدة الصور التي تم حذفها من انستقرام</p>
                            <div class="ad-btn">مشاهدة الآن قبل الحذف 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مشاهير العرب | تريند النجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #080808; --card: #121212; --main: #ff0055; --gold: #ffd700; --text: #ffffff; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--bg); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        header {{ background: rgba(0,0,0,0.95); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--main); display: flex; justify-content: center; }}
        .logo {{ font-size: 26px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--main); }}
        .ticker-bar {{ position: fixed; top: 76px; width: 100%; background: var(--main); color: #fff; height: 35px; display: flex; align-items: center; z-index: 999; overflow: hidden; }}
        .ticker-label {{ background: #000; padding: 0 15px; font-weight: 900; height: 100%; display: flex; align-items: center; font-size: 12px; }}
        .ticker-content {{ white-space: nowrap; animation: scroll 40s linear infinite; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-350%); }} }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 20px; }}
        .celeb-card {{ background: var(--card); border-radius: 12px; overflow: hidden; border: 1px solid #222; position: relative; transition: 0.3s; }}
        .celeb-card:hover {{ transform: translateY(-5px); border-color: var(--main); box-shadow: 0 5px 15px rgba(255,0,85,0.2); }}
        .trending-badge {{ position: absolute; top: 12px; right: 12px; background: var(--main); color: #fff; padding: 3px 12px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 5; }}
        .img-wrapper {{ height: 240px; overflow: hidden; border-bottom: 2px solid var(--main); }}
        .img-wrapper img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .card-content {{ padding: 20px; }}
        .card-title {{ font-size: 18px; font-weight: 700; height: 52px; overflow: hidden; margin-bottom: 15px; line-height: 1.5; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        .btn-primary {{ display: block; background: var(--main); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: 900; }}
        .vip-ad-box {{ grid-column: 1 / -1; background: linear-gradient(135deg, #1a1a1a, #000); border: 2px solid var(--gold); border-radius: 15px; padding: 40px; text-align: center; }}
        .ad-btn {{ background: #fff; color: #000; display: inline-block; padding: 12px 40px; border-radius: 50px; font-weight: 900; margin-top: 15px; text-decoration: none; }}
        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header><a href="#" class="logo">CELEB<span>ARAB</span></a></header>
    <div class="ticker-bar"><div class="ticker-label">عاجل والآن</div><div class="ticker-content">{ticker_items}</div></div>
    <main class="container">{news_html}</main>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celebrity_mission()
