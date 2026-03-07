import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celeb_scraper():
    rss_url = "https://www.sayidaty.net/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الربحي الخاص بك
        my_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"✨ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:35]):
            title = item.title.text
            link = item.link.text
            
            # استخراج الصورة الحقيقية بدقة
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            if not img_url and item.description:
                img_match = re.search(r'<img src="(.*?)"', item.description.text)
                if img_match:
                    img_url = img_match.group(1)
            
            if not img_url:
                img_url = "https://www.sayidaty.net/themes/custom/sayidaty/logo.png"

            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">تريند اليوم</div>
                <div class="card-thumb">
                    <a href="{my_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Celebrity News">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>🎬 مشاهير وأضواء</span>
                        <span>📅 {datetime.now().strftime("%d/%m/%Y")}</span>
                    </div>
                    <a href="{my_link}" target="_blank" class="btn-main">التفاصيل الكاملة 👁️‍🗨️</a>
                </div>
            </article>'''

            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="premium-ad">
                    <a href="{my_link}" target="_blank">
                        <div class="ad-content">
                            <span class="exclusive-label">حصري VIP</span>
                            <h3>فضيحة تهز أوساط المشاهير قبل قليل!</h3>
                            <p>شاهد الصور المسربة التي تم حذفها فوراً</p>
                            <div class="ad-btn">دخول السيرفر السري 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مشاهير لايف | أخبار النجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #e91e63; --gold: #ffc107; --bg: #0d0d0d; --card: #1a1a1a; --text: #ffffff; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--bg); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        header {{ background: rgba(0,0,0,0.95); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--main); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 26px; font-weight: 900; text-decoration: none; color: #fff; }}
        .logo span {{ color: var(--main); }}
        .ticker {{ position: fixed; top: 76px; width: 100%; background: #fff; color: #000; height: 35px; display: flex; align-items: center; z-index: 999; overflow: hidden; border-bottom: 2px solid var(--gold); }}
        .ticker-label {{ background: var(--main); color: #fff; padding: 0 15px; font-weight: 900; height: 100%; display: flex; align-items: center; font-size: 13px; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 40s linear infinite; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-300%); }} }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 20px; }}
        .celeb-card {{ background: var(--card); border-radius: 15px; overflow: hidden; border: 1px solid #333; transition: 0.3s; position: relative; }}
        .celeb-card:hover {{ transform: translateY(-5px); border-color: var(--main); }}
        .trend-tag {{ position: absolute; top: 12px; right: 12px; background: var(--main); color: #fff; padding: 3px 12px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 5; }}
        .card-thumb {{ height: 250px; overflow: hidden; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .card-body {{ padding: 18px; }}
        .card-title {{ font-size: 18px; font-weight: 700; height: 52px; overflow: hidden; line-height: 1.5; margin-bottom: 15px; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 15px; }}
        .btn-main {{ display: block; background: var(--main); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: 900; }}
        .premium-ad {{ grid-column: 1 / -1; background: linear-gradient(135deg, #e91e63, #880e4f); border-radius: 15px; padding: 40px; text-align: center; }}
        .ad-btn {{ background: #fff; color: var(--main); display: inline-block; padding: 12px 35px; border-radius: 50px; font-weight: 900; margin-top: 20px; text-decoration: none; }}
        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header><a href="#" class="logo">CELEB<span>LIVE</span></a></header>
    <div class="ticker"><div class="ticker-label">عاجل</div><div class="ticker-text">{ticker_items}</div></div>
    <main class="container">{news_html}</main>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celeb_scraper()
