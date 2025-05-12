import numpy as np
import pandas as pd
import json
import random
import operator
##### Chapter 2. 알고리즘
### 1. 코사인유사도
# 받게되는 유저의 정보는 크게 5가지 이다.
# userinfo[0] = pice ( 0 ~ 4 )
# 0 = 최저~30 [203개] // 1 = 30~50 [269개] // 2 = 50~80 [525개] // 3 = 80~130 [470개] // 4 = 130~최대 [533개]
#  
# userinfo[1] = country ( 0 ~ 6 )
# 0 = france // 1 = italy // 2 = spain // 3 = australia // 4 = argentina // 5 = us // 6 = etc
# 
# userinfo[2] = wine종류 ( 0 ~ 1)
# 0 = red // 1 = white
# 
# userinfo[3] = winedetail #1 ( 0 ~ 2 )
# userinfo[4] = winedetail #2 ( 0 ~ 1 )
#
# 끝 3개 요소를 보면 와인맛을 알 수 있다.
# 0,0,0 = Light and Perfumed
# 0,0,1 = Rich and Intense
# 0,1,0 = Bold and Structured
# 0,1,1 = Savory and Classic
# 1,0,0 = Aromatic and Floral
# 1,0,1 = Green and Flinty
# 1,0,2 = Tropical and Balanced
# 1,1,0 = Buttery and Complex
# 1,1,1 = Dry and Nutty
#
## 결론 : 리스트형태로 [ (0~4사이숫자) , (0~6사이숫자) , (0~1사이숫자) , (0~2사이숫자) , (0~1사이숫자) ]


# 가공이 필요
#               가격 나라 종류 과일 음식 맛
# userinfo = [0,0,0,0,0,|0,0,0,0,0,0,0,|0,|0,|0,|0,0,|0  ]
#  Beginner = 1,0,0,0,0
#  Party    = 0,1,0,0,0
#  France   =            1,0,0,0,0,0,0
#  Italy    =            0,1,0,0,0,0,0  
#  red      =                           0
#  white    =                           1
#  fruity O =                              0
#  fruity X =                              1  
#  food O   =                                 0  
#  food X   =                                 1
#  sweet    =                                    0,1 
#  fresh    =                                    1,0
#  any      =                                    1,1
#  creamy   =                                         0            
#  dry      =                                         1 
## 맛은 트로피칼같은경우 달달하기도하고 상큼하기도 때문에 추가적인 추천방법을 위해 두 값을 모두 갖도록 했다.
## 이걸 문자를 읽지않고 번거롭게 벡터화시킨 이유는 글만으로는 두 맛의 유사도를 알 수 없기 때문이다. 따라서 일부러 설정을 해줬다.
with open("BE/userinfo.json","r") as json_file:
    info = json.load(json_file)

new = info[1:-1].split(",")
usertemp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
userinfo = []
for i in range(len(new)):
    userinfo.append(int(new[i]))

## 임시유저정보로 frontend에서 받아오게 될 것이다.
# 여기서 가격별로 달리 추천할거 / 맛별로 달리 추천할거 생각하자
# (1) 맛 추천 (같은항목(레드-레드))
# 0,0,0 = Light and Perfumed       <>   0,0,1 = Rich and Intense
# 0,1,0 = Bold and Structured  #    <>   0,1,1 = Savory and Classic
# 1,0,0 = Aromatic and Floral  #    <>   1,0,1 = Green and Flinty    <>    1,0,2 = Tropical and Balanced >> 랜덤으로 추천하자
# 1,1,0 = Buttery and Complex      <>   1,1,1 = Dry and Nutty 

##############################미정

# (2) 맛 추천 (다른항목(레드-화이트))
# 0,0,0 = Light and Perfumed       <>   1,0,0 = Aromatic and Floral <>    1,0,2 = Tropical and Balanced >> 랜덤으로 추천하자
# 0,0,1 = Rich and Intense         <>   1,0,1 = Green and Flinty    <>    1,0,2 = Tropical and Balanced >> 랜덤으로 추천하자
# 0,1,0 = Bold and Structured      <>   1,1,1 = Dry and Nutty 
# 0,1,1 = Savory and Classic       <>   1,1,0 = Buttery and Complex

##############################미정

# (3) 가격 추천
# 0인 가격 추천
# 1단계 높은 가격 추천
# 1단계 낮은 가격 추천 



temp = 0
for num in userinfo:
    if(temp == 0):
        usertemp[num] = 1
        temp += 1
    elif(temp == 1):
        usertemp[5+num] = 1
        temp += 1
    elif(temp == 2):
        usertemp[12] = num
        if(num == 0):
            temp += 1
            # red 질문
        else:
            temp += 4
            # white 질문
    elif(temp == 3):
    # red
        usertemp[13] = num
        if(num == 0):
            temp += 1
        else:
            temp += 2
    elif(temp == 4):
    # red 2
        usertemp[14] = num
        if(num == 0):
            usertemp[16] = 1
        else:
            usertemp[15] = 1 
    elif(temp == 5):
    # red 2
        usertemp[14] = num    
    elif(temp == 6):
    # white
        usertemp[13] = num
        if(num == 0):
            temp += 1
        else:
            temp += 2
    elif(temp == 7):
    # white 2
        if(num == 2):
            usertemp[15] = 1
            usertemp[16] = 1
        else:
            usertemp[16-num] = 1         
    elif(temp == 8):
        usertemp[17] = num

# 이제 유저도 winedata['array']처럼 벡터로 이루어졌다.
# 이제 비교하면서 코사인 유사도를 찾을 것이다.
print("Vector array of user is "+str(usertemp))
df = pd.read_csv("BE/winedata3.csv")


count = 0
recommendwine = {}
maxnum = 0

pweight = 1/3
cweight = 1/6
tweight = 1/2


for array in df['array']:
    newarray = array[1:-1].split(",")
    mom1 = 0
    mom2 = 0
    son = 0
    for index in range(5):  
        mom1 += int(newarray[index])**2
        mom2 += usertemp[index]**2
        son += usertemp[index] * int(newarray[index])
    mom = (mom1**0.5)*(mom2**0.5)
    pricecos = (son/mom)
    
    mom1 = 0
    mom2 = 0
    son = 0
    for index in range(7):
        mom1 += int(newarray[5+index])**2
        mom2 += usertemp[5+index]**2
        son += usertemp[5+index] * int(newarray[5+index])
    mom = (mom1**0.5)*(mom2**0.5)
    countrycos = (son/mom)

    mom1 = 0
    mom2 = 0
    son = 0
    tastecos = 0
    if( int(newarray[-1]) == 0):
        for index in range(6):
            mom1 += int(newarray[12+index])**2
            mom2 += usertemp[12+index]**2
            son += usertemp[12+index] * int(newarray[12+index])
        mom = (mom1**0.5)*(mom2**0.5)
        tastecos += (son/mom)
    #print(max(maxnum, pricecos+countrycos+tastecos))
    
    pricecos *= pweight
    countrycos *= cweight
    tastecos *= tweight
    point = pricecos+countrycos+tastecos

    if(maxnum < pricecos+countrycos+tastecos):
        recommendwine.clear()
        maxnum = pricecos+countrycos+tastecos
        recommendwine[str(count)] = int(df['points'][count])
    elif(maxnum == pricecos+countrycos+tastecos):
        maxnum = pricecos+countrycos+tastecos
        recommendwine[str(count)] = int(df['points'][count])

    
    #print(str(count) + " / " + str(pricecos) + " / " + str(countrycos) + " / " + str(tastecos))
    count += 1
# 이렇게 코사인유사도를 나눈 이유는 우리가 가진 데이터가 편향되어있기 때문이다.
# 따라서 우리가 적게가지고 있는 것을 선택했을 때 그곳에 가중치를 더 두어 보다 정확한 유사도를 얻기 위함이다.
# 예를 들면 나라가 다르고 

gotoresult = []


if(len(recommendwine) > 3):
    newrecommend = random.sample(recommendwine.keys(),3)
    for wineindex in newrecommend:
        result = {'index':wineindex ,'name':df['title'][int(wineindex)],'country':df['country'][int(wineindex)],'price':df['price'][int(wineindex)],'taste':df['taste'][int(wineindex)]}
        gotoresult.append(result)

else:
    for wineindex in recommendwine:
        result = {'index':wineindex ,'name':df['title'][int(wineindex)],'country':df['country'][int(wineindex)],'price':df['price'][int(wineindex)],'taste':df['taste'][int(wineindex)]}
        gotoresult.append(result)


with open("BE/recommend.json","w")as json_file:
    json.dump(gotoresult,json_file)


# 지금 하고자하는 거 = 맛은 똑같을 때 가격대같고 나라다른거 / 가격대다르고 나라같은거 >> 두개가 같은 유사도로 나오기 때문에

################미정 ++ 이 후 평가 페이지에서 다시 받아오고 점수를 업데이트 시켜야하므로 인덱스 넘버를 추가해야한다. === count 
############# + 유저가 들어오면 유사도 검사를 실행할지 아니면 와인끼리 유사도검사를 미리 실행하고 진행할지
############# + 유저 고유 id값을 받으면 그 id의 기록들을 따로 남겨 이 기록들을 통해 collaborative filtering 도 하도록
