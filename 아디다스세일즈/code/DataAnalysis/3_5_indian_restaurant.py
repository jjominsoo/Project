import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def indian_restaurant2():
    res = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석/DataAnalysis/3주차/5일차/indian_restaurant2.csv',
                      encoding='unicode_escape')
    print(res.head(2))
    res_1 = res[res['cnt'] == 1]
    res_2 = res[res['cnt'] == 2]
    res_ov3 = res[res['cnt'] > 2]

    res_2 = res_2.groupby('restaurant_name').mean().reset_index()
    res_ov3 = res_ov3.groupby('restaurant_name').mean().reset_index()

    bins = np.linspace(2, 5, 30)
    plt.hist(res_1['rating'], bins, alpha=0.5, label='1', density=True)
    plt.hist(res_2['rating'], bins, alpha=0.5, label='2', density=True)
    plt.hist(res_ov3['rating'], bins, alpha=0.5, label='ov3', density=True)

    plt.legend(loc='upper right')
    plt.show()

def indian_restaurant4():
    data = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석/DataAnalysis/3주차/5일차/indian_restaurant4.csv',
                      encoding='unicode_escape')
    print(data.head(2))
    data_1 = data[data['cnt'] == 1]
    data_2 = data[data['cnt'] == 2]
    data_ov3 = data[data['cnt'] > 2]

    print(f"점포 수 1개일 때 가격과 별점의 상관계수 : {np.corrcoef(data_1['rating'], data_1['average_price'])[0,1]}")
    print(f"점포 수 1개일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(data_1['rating'], data_1['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"점포 수 2개일 때 가격과 별점의 상관계수 : {np.corrcoef(data_2['rating'], data_2['average_price'])[0, 1]}")
    print(f"점포 수 2개일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(data_2['rating'], data_2['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"점포 수 3개 이상일 때 가격과 별점의 상관계수 : {np.corrcoef(data_ov3['rating'], data_ov3['average_price'])[0, 1]}")
    print(f"점포 수 3개 이상일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(data_ov3['rating'], data_ov3['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")

    non_fast = data[data['fast_food_or_not'] == 0]
    fast = data[data['fast_food_or_not'] == 1]
    print(f"패스트푸드점이 아닐 때 가격과 별점의 상관계수 : {np.corrcoef(non_fast['rating'], non_fast['average_price'])[0, 1]}")
    print(f"패스트푸드점이 아닐 때 배달 시간과 별점의 상관계수 : {np.corrcoef(non_fast['rating'], non_fast['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"패스트푸드점일 때 가격과 별점의 상관계수 : {np.corrcoef(fast['rating'], fast['average_price'])[0, 1]}")
    print(f"패스트푸드점일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(fast['rating'], fast['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")

    non_street = data[data['street_food'] == 0]
    street = data[data['street_food'] == 1]
    print(f"길거리음식점이 아닐 때 가격과 별점의 상관계수 : {np.corrcoef(non_street['rating'], non_street['average_price'])[0, 1]}")
    print(f"길거리음식점이 아닐 때 배달 시간과 별점의 상관계수 : {np.corrcoef(non_street['rating'], non_street['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"길거리음식점일 때 가격과 별점의 상관계수 : {np.corrcoef(street['rating'], street['average_price'])[0, 1]}")
    print(f"길거리음식점일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(street['rating'], street['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")

    non_bakery = data[data['bakery_or_not'] == 0]
    bakery = data[data['bakery_or_not'] == 1]
    print(f"베이커리가 아닐 때 가격과 별점의 상관계수 : {np.corrcoef(non_bakery['rating'], non_bakery['average_price'])[0, 1]}")
    print(f"베이커리가 아닐 때 배달 시간과 별점의 상관계수 : {np.corrcoef(non_bakery['rating'], non_bakery['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"베이커리일 때 가격과 별점의 상관계수 : {np.corrcoef(bakery['rating'], bakery['average_price'])[0, 1]}")
    print(f"베이커리일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(bakery['rating'], bakery['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")

def indian_restaurant5_6():
    data = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석/DataAnalysis/3주차/5일차/indian_restaurant4.csv',
                       encoding='unicode_escape')
    big = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석/DataAnalysis/3주차/5일차/indian_restaurant5.csv',
                      encoding='unicode_escape')
    small = pd.read_csv('C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석/DataAnalysis/3주차/5일차/indian_restaurant6.csv',
                      encoding='unicode_escape')

    big_cities = data[data['location'].isin(big['location'])]
    small_cities = data[data['location'].isin(small['location'])]
    print(f"대도시일 때 가격과 별점의 상관계수 : {np.corrcoef(big_cities['rating'], big_cities['average_price'])[0, 1]}")
    print(f"대도시일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(big_cities['rating'], big_cities['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
    print(f"소도시일 때 가격과 별점의 상관계수 : {np.corrcoef(small_cities['rating'], small_cities['average_price'])[0, 1]}")
    print(f"소도시일 때 배달 시간과 별점의 상관계수 : {np.corrcoef(small_cities['rating'], small_cities['average_delivery_time'])[0, 1]}")
    print("----------------------------------------------")
# indian_restaurant2()
# indian_restaurant4()
indian_restaurant5_6()