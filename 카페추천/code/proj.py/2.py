from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import pandas as pd
import numpy as np


# csv 파일이되 데이터 구분을 '|' 로 해둔 파일입니다. sep 지정을 안 하면 읽을 수 없습니다.
df = pd.read_csv('소상공인시장진흥공단_상가(상권)정보_서울_202206.csv', sep='|')  

driver = webdriver.Chrome("./chromedriver") 

# 포스팅 작성 당시 크롬 버젼 : 92

df = df.loc[df["상권업종대분류명"] == '음식']  

# 다음과 같은 칼럼만 있으면 됩니다
df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

# 그 중에서도 흑석동과 상도1동만 쓸 겁니다.
df = df.loc[(df['행정동명'] == '흑석동') | (df['행정동명'] == '상도1동')]

df.columns = ['name',  # 상호명
              'cate_1',  # 중분류명
              'cate_2',  # 소분류명
              'cate_3',  # 표준산업분류명
              'dong',  # 행정동명
              'lon',  # 위도
              'lat'  # 경도
              ]

df['cate_mix'] = df['cate_1'] + df['cate_2'] +  df['cate_3']
df['cate_mix'] = df['cate_mix'].str.replace("/", " ")

from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도


count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
place_category = count_vect_category.fit_transform(df['cate_mix']) 
place_simi_cate = cosine_similarity(place_category, place_category) 
place_simi_cate_sorted_ind = place_simi_cate.argsort()[:, ::-1]

# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.

df['naver_keyword'] = df['dong'] + "%20" + df['name']  # "%20"는 띄어쓰기를 의미합니다.
df['naver_map_url'] = ''


# 본격적으로 가게 상세페이지의 URL을 가져옵시다

for i, keyword in enumerate(df['naver_keyword'].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] -1} 행", keyword)
    try:
        naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={keyword}&sm=hty&style=v5"
        
        driver.get(naver_map_search_url)
        time.sleep(3.5)
        df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
        # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
        # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
        
        #만약 검색 결과가 없다면?
    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
                time.sleep(1)
            except Exception as e2:
                print(e2)
                df.iloc[i,-1] = np.nan
                time.sleep(1)
        else:
            pass


driver.quit()


# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url']


# URL이 수집되지 않은 데이터는 제거합니다.
df = df.loc[~df['naver_map_url'].isnull()]