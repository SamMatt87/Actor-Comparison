from bs4 import BeautifulSoup
from requests import get
import re
def get_search_page(name):
    url='https://www.imdb.com/search/name/?name='+'+'.join(name.split())
    return url
def actor_page(name):
    response=get(get_search_page(name))
    soup=BeautifulSoup(response.text,'html.parser')
    id=soup.h3.a.get('href')
    return 'https://www.imdb.com'+id
def movie_list(name):
    response = get(actor_page(name))
    soup = BeautifulSoup(response.text, 'html.parser')
    roles=soup.find_all(id=re.compile("^actor"))
    movies=[]
    year=[]
    for i in roles:
        movies.append(i.find('a').get_text())
        year.append(i.find('span').get_text()[2:-1])
    return list(zip(movies,year))
