import pandas as pd
import numpy as np

##### Chapter 1. 데이터가공
### 1. 예외처리
# price = 비어있는 셀 (nan값) 들은 0으로 통일하고 
# country = 보기에 주어진 나라 외는 전부 ETC로 분류
# title = 크롤링 하기 쉽도록, (1)빈칸을 +로 대체 (2)괄호 제거
# 데이터는 일단 보존시키기 위해 새로운 csv파일로 저장햇다 (windata2.csv)

df = pd.read_csv("winedata.csv")

for country in df['country']:
    if(country != "France" and country != "Italy" and country != "Spain" and country != "Australia" and country != "Argentina" and country != "US"):
        newstring = "ETC"
        df['country'] = df['country'].replace(country, newstring)

for price in df['price']:
    if(np.isnan(price)):
        df['price'] = df['price'].replace(price, 0)

for wine in df['title']:
    newstring = ''.join([i for i in wine if not i.isdigit()])
    newstring = newstring.replace(" ","+" )
    newstring = newstring.replace("(","" )
    newstring = newstring.replace(")","" )

    df['title'] = df['title'].replace(wine, newstring)


df.to_csv("winedata2.csv",sep=",", index=False)

# 봐야할것 1. price 2. country 3. taste





