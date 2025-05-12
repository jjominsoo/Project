import requests as rq
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from requests.api import head, request
import pandas as pd
from fake_useragent import UserAgent

from random import randrange
### 2. 크롤링
# 앞선 process1에서 가공한 데이터를 가지고 새로운 데이터를 얻기위해 크롤링을 실시한다.
# 지금 오류가 난다 (403 권한에러)
# 이걸 해결하는 과정을 풀어나가는 것도 좋을 것 같다.

df = pd.read_csv("BE/winedata3.csv")


tastelist = []
url1 = "https://www.wine-searcher.com/find/"
#winename2 = "Terre+di+Giurfo+Belsito+Frappato"
winename = "Rainstorm+Pinot+Gris"
tag = "#t2"


# 셀레니움
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")
#options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe',options=options)
print(driver)
driver.get("https://www.wine-searcher.com/")
#driver.get(url1 + winename)
search = driver.find_element_by_name("Xwinename")
search.send_keys(winename)
search.send_keys(Keys.ENTER)
r = driver.find_element_by_xpath('//*[@id="find-tab-info"]').click()
time.sleep(30)
#print(r[1].get_attribute('href = #tab-info'))
#print(r)
#driver.close()
#driver.quit()


"""
# 뷰티풀소프

for winename in df['title']:
    ua = UserAgent()
    hdr = {'User-Agent': ua.random} 
    print(winename)
    r =  rq.get(url1 + winename +  tag,headers=hdr)
    print(r)
    time.sleep(1)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        time.sleep(1)
        result1 = soup.find_all('a', 'd-flex pb-4')
        tastelist.append(result1[1]["href"][10:])
        time.sleep(2)
    except IndexError as e:
        tastelist.append("")
    print(tastelist)


df['taste'] = ""
for i in range(len(df['taste'])):
    number = randrange(10)
    if(number == 0):
        df['taste'][i] = "red-light-and-perfumed"
    elif(number == 1):
        df['taste'][i] = "red-rich-and-intense"
    elif(number == 2):
        df['taste'][i] = "red-bold-and-structured"
    elif(number == 3):
        df['taste'][i] = "red-savory-and-classic"
    elif(number == 4):
        df['taste'][i] = "white-aromatic-and-floral"
    elif(number == 5):
        df['taste'][i] = "white-green-and-flinty"
    elif(number == 6):
        df['taste'][i] = "white-tropical-and-balanced"
    elif(number == 7):
        df['taste'][i] = "white-buttery-and-complex"
    elif(number == 8):
        df['taste'][i] = "white-dry-and-nutty"
    else:
        df['taste'][i] = ""
        """
#df['taste'] = tastelist
df.to_csv("BE/winedata3.csv",sep=",", index=False)


