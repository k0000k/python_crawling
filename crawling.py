from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pokemonkorea.co.kr/")
bsObject = BeautifulSoup(html, "lxml")

news = bsObject.select(
    '#ct > section.sect-news.bg-pattern.grid2 > div > ul > li')

for item in news:
    link = item.select_one(
        "#ct > section.sect-news.bg-pattern.grid2 > div > ul > li > a")["href"]
    if (link[0:5] == '/news'):
        link = 'https://www.pokemonkorea.co.kr'+link
    elif (link[0:17] == '/pokemoncaferemix'):
        link = 'https://pokemonkorea.co.kr/'+link
    print(link)
