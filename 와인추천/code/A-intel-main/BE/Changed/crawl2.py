import requests
from bs4 import BeautifulSoup

from requests.api import head

url1 = "https://www.vivino.com/search/wines?q="
winename2 = "Terre+di+Giurfo+Belsito+Frappato"
winename = "Rainstorm+Pinot+Gris"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get(url1 + winename2,headers=headers).text
soup = BeautifulSoup(data, 'html.parser')

result1 = soup.find_all('section')
winelink = result1[0].find('a')["href"]
print(winelink)
url2 = "https://www.vivino.com/US-CA/en/"


data2 = requests.get(url2 + winelink, headers=headers).text
soup2 = BeautifulSoup(data2, 'html.parser')

result2 = soup2.find_all(attrs={"class":"lower"})
