from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pokemonkorea.co.kr/")
bsObject = BeautifulSoup(html, "html.parser")

news = bsObject.select('#ct > section.sect-news.bg-pattern.grid2 > div > ul > li')

for item in news:
    link=item.select_one("#ct > section.sect-news.bg-pattern.grid2 > div > ul > li > a")["href"]
    print(link)
