from bs4 import BeautifulSoup as bs
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
print(req)
html = req.read()

soup = bs(html, 'html.parser')
news = soup.find_all('li', class_="liga-news-item")

results = []

for item in news:
    title = item.find('span', class_="d-block").get_text(strip=True)
    print(title)
    desk = None
    link = None