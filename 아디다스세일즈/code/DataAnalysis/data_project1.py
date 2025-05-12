import pandas as pd
import numpy as np
# data = pd.read_csv("C:/Users/jjomi/OneDrive/바탕 화면/데브코스-데이터분석2/4주차/data_sales (1).csv")
data = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석2/4주차/data_sales (1).csv")
print(data.columns)

data['Retailer'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Retailer']):
    # if i == 0:
    #     print(f"Retailer : {type(d)}")
    new_d = d.lower().replace(" ","").replace("\'","")
    data.loc[i, 'Retailer'] = new_d

data['Retailer ID'].fillna(0,inplace=True)
id_list = [1128299,1185732,1189833,1197831]
id_list = []
for i,d in enumerate(data['Retailer ID']):
    # if i == 0:
    #     print(f"Retailer ID : {type(d)}")
    if d not in id_list:
        id_list.append(d)
    new_d = id_list.index(d)
    data.loc[i, 'Retailer ID'] = new_d

data['Invoice Date'].fillna("0001-01-01",inplace=True)
for i,d in enumerate(data['Invoice Date']):
    # if i == 0:
    #     print(f"Invoice Date : {type(d)}")
    a = d.split('/')
    temp = a[2]
    temp2 = a[1]
    a[1] = a[0]
    a[2] = temp2
    a[0] = temp
    new_d = '-'.join(a)
    data.loc[i,'Invoice Date'] = new_d
data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])


data['Region'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Region']):
    # if i == 0:
    #     print(f"Region : {type(d)}")
    temp_d = d.lower()
    if temp_d == 'midwest':
        new_d = 'mw'
    elif temp_d == 'northeast':
        new_d = 'ne'
    elif temp_d == 'south':
        new_d = 's'
    elif temp_d == 'southeast':
        new_d = 'se'
    elif temp_d == 'west':
        new_d = 'w'
    else:
        new_d = d
    data.loc[i,'Region'] = new_d


data['State'].fillna("ETC",inplace=True)
for i,d in enumerate(data['State']):
    # if i == 0:
    #     print(f"State : {type(d)}")
    new_d = d.replace(" ","").lower()
    data.loc[i,'State'] = new_d


data['City'].fillna("ETC",inplace=True)
for i,d in enumerate(data['City']):
    # if i == 0:
    #     print(f"City : {type(d)}")
    new_d = d.replace(" ","").lower()
    data.loc[i,'City'] = new_d

data['Product'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Product']):
    # if i == 0:
    #     print(f"Product : {type(d)}")
    temp_d = d.lower()
    if 'women' in temp_d:
        if 'footwear' in temp_d:
            if 'athletic' in temp_d:
                new_d = "waf"
            else:
                new_d = "wsf"
        else:
            new_d = "wa"
    else:
        if 'footwear' in temp_d:
            if 'athletic' in temp_d:
                new_d = "maf"
            else:
                new_d = "msf"
        else:
            new_d = "ma"
    data.loc[i,'Product'] = new_d


data['Price per Unit'].fillna(0,inplace=True)
for i,d in enumerate(data['Price per Unit']):
    # if i == 0:
    #     print(f"Price per Unit : {type(d)}")
    if d == 0:
        new_d = 0
    else:
        new_d = int(d[1:-4])
    data.loc[i,'Price per Unit'] = int(new_d)
data['Price per Unit'] = data['Price per Unit'].astype(int)

data['Units Sold'].fillna(0,inplace=True)
for i,d in enumerate(data['Units Sold']):
    # if i == 0:
    #     print(f"Units Sold : {type(d)}")
    new_d = int(d.replace(',',""))
    data.loc[i,'Units Sold'] = new_d
data['Units Sold'] = data['Units Sold'].astype(int)

data['Total Sales'].fillna(0,inplace=True)
for i,d in enumerate(data['Total Sales']):
    # if i == 0:
    #     print(f"Total Sales : {type(d)}")
    new_d = d
    if not d.isdigit():
        new_d = int(d.replace(',',""))
    data.loc[i,'Total Sales'] = int(new_d)
data['Total Sales'] = data['Total Sales'].astype(int)

data['Operating Profit'].fillna(0,inplace=True)
for i,d in enumerate(data['Operating Profit']):
    # if i == 0:
    #     print(f"Operating Profit : {type(d)}")
    new_d = int(d.replace(',',"").replace("$",""))
    data.loc[i,'Operating Profit'] = int(new_d)
data['Operating Profit'] = data['Operating Profit'].astype(int)

data['Sales Method'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Sales Method']):
    # if i == 0:
    #     print(f"Sales Method : {type(d)}")
    temp_d = d.lower()
    if 'online' in temp_d:
        new_d = "on"
    elif 'outlet' in temp_d:
        new_d = 'out'
    else:
        new_d = "in"
    data.loc[i,'Sales Method'] = new_d



with pd.option_context('display.max_columns',None):
    print(data.head(10))
    print(data.dtypes)

data.to_csv("C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석2/4주차/adidas_sales.csv",index=False)
## 1차 전처리 완료
## 일단 Retailer, Region 다 약어로 고쳐보자
## State, City는 소문자로 그냥 통일