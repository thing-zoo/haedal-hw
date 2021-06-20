import requests
import bs4

headers ={
  'User-Agent': 'Not_Crawling X)' 
}

url = 'https://kin.naver.com'

try:
    page = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(page, 'html.parser')
    rankings = soup.select('#rankingChart > ul > .ranking_item')
    items = []
    for item in rankings:
        n = item.select_one('.no').text
        title = item.select_one('.ranking_title').text
        items.append((n, title))
        
    items = sorted(items, key = lambda x: int(x[0]))
except requests.ConnectionError:
    print('requst get error')


with open('python/hw6/kin_rank.csv', 'w') as f:
    for item in items:
        f.write(f'{item[0]}위, {item[1]}\n')
