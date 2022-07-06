from urllib.request import urlopen
from bs4 import BeautifulSoup

pokemonHtml = urlopen("https://pokemonkorea.co.kr/")
pokemonBs = BeautifulSoup(pokemonHtml, "lxml")

pokemonNews = pokemonBs.select(
    '#ct > section.sect-news.bg-pattern.grid2 > div > ul > li')

for item in pokemonNews:
    link = item.select_one(
        "#ct > section.sect-news.bg-pattern.grid2 > div > ul > li > a")["href"]
    if (link[0:5] == '/news'):
        link = 'https://www.pokemonkorea.co.kr'+link
    elif (link[0:17] == '/pokemoncaferemix'):
        link = 'https://pokemonkorea.co.kr/'+link
    print(link)


nintendoHtml = urlopen("https://www.nintendo.co.kr/news/list.php")
nintendoBs = BeautifulSoup(nintendoHtml, "lxml")

nintendoNews = nintendoBs.select(
    'body > section.contents.news_page > div.news_list.article > div > div')

for item in nintendoNews:
    link = item.select_one(
        "body > section.contents.news_page > div.news_list.article > div > div > a")["href"]
    #어렵네요 닌텐도 웹페이지는...
    
