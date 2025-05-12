import requests as rq
from bs4 import BeautifulSoup


from requests.api import head

url1 = "https://www.wine-searcher.com/find/"
winename2 = "Terre+di+Giurfo+Belsito+Frappato"
winename = "Rainstorm+Pinot+Gris"
tag = "#t2"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


r=  rq.get(url1 + winename + tag,headers=headers)
# data = rq.get(url1 + winename + tag, headers=headers)
print(r)
# print(data)

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup)

result1 = soup.find_all('a', 'd-flex pb-4')
print(result1)
