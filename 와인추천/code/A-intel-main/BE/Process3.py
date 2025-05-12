import pandas as pd
import numpy as np


### 3. 재가공
# 결국 코사인유사도를 진행하기 위해서 다시 가공해야한다.
# 어차피 맛값을 받아 그것도 벡터화 시켜야햇기 때문에 한번에 진행했다.
# 지금은 값이 대괄호도 같이 저장되어서 ( [ 0 , ~~ , 0 ] ) 실제 계산에는 양끝값 ([ ])를 빼야한다. >> 나중에 손봐야한다.
# 결국 마지막에 array 열에 내가 원하는ㅡ코사인유사도를위한 배열이 저장된다.



df = pd.read_csv("BE/winedata3.csv")

winelist = []

for price in df['price']:
    if(20 <= price and price < 30):
        winelist.append([1,0,0,0,0])
    elif(30 <= price and price < 50):
        winelist.append([0,1,0,0,0])
    elif(50 <= price and price < 80):
        winelist.append([0,0,1,0,0])
    elif(80 <= price and price < 130):
        winelist.append([0,0,0,1,0])
    elif(130 <= price or price == 0):
        winelist.append([0,0,0,0,1])

index = 0
for country in df['country']:
    if(country == "France"):
        winelist[index].extend([1,0,0,0,0,0,0])
    elif(country == "Italy"):
        winelist[index].extend([0,1,0,0,0,0,0])
    elif(country == "Spain"):
        winelist[index].extend([0,0,1,0,0,0,0])
    elif(country == "Australia"):
        winelist[index].extend([0,0,0,1,0,0,0])
    elif(country == "Argentina"):
        winelist[index].extend([0,0,0,0,1,0,0])
    elif(country == "US"):
        winelist[index].extend([0,0,0,0,0,1,0])
    elif(country == "ETC"):
        winelist[index].extend([0,0,0,0,0,0,1])
    index += 1

index = 0
for taste in df['taste']:
    if(taste == "red-light-and-perfumed"):
        winelist[index].extend([0,0,0,0,1,0,0]) #00000
    elif(taste == "red-rich-and-intense"):
        winelist[index].extend([0,0,1,1,0,0,0]) #00001
    elif(taste == "red-bold-and-structured"):
        winelist[index].extend([0,1,0,0,0,0,0])
    elif(taste == "red-savory-and-classic"):
        winelist[index].extend([0,1,1,0,0,0,0])
    elif(taste == "white-aromatic-and-floral"):
        winelist[index].extend([1,0,0,0,1,0,0])
    elif(taste == "white-green-and-flinty"):
        winelist[index].extend([1,0,0,1,0,0,0])
    elif(taste == "white-tropical-and-balanced"):
        winelist[index].extend([1,0,0,1,1,0,0])
    elif(taste == "white-buttery-and-complex"):
        winelist[index].extend([1,1,0,0,0,0,0])
    elif(taste == "white-dry-and-nutty"):
        winelist[index].extend([1,1,0,0,0,1,0])
    else:
        winelist[index].extend([0,0,0,0,0,0,1])
    index += 1
                        # 백퍼 오류나는데 일단 스킵
df['array'] = winelist

df.to_csv("BE/winedata3.csv",sep=",", index=False)