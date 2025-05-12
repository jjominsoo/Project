import pandas as pd
import numpy as np

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

# Taste에 크롤링한거 집어넣자

df['taste'] = "red-rich-and-Intense"




# 봐야할것 1. price 2. country 3. taste
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
        winelist[index].extend([0,0,0,0,0,0])
    elif(taste == "red-rich-and-Intense"):
        winelist[index].extend([0,0,1,0,0,0])
    elif(taste == "red-bold-and-structured"):
        winelist[index].extend([0,1,0,0,0,0])
    elif(taste == "red-savory-and-slassic"):
        winelist[index].extend([0,1,1,0,0,0])
    elif(taste == "white-aromatic-and-floral"):
        winelist[index].extend([1,0,0,0,1,0])
    elif(taste == "white-green-and-flinty"):
        winelist[index].extend([1,0,0,1,0,0])
    elif(taste == "white-tropical-and-balanced"):
        winelist[index].extend([1,0,0,1,1,0])
    elif(taste == "white-buttery-and-complex"):
        winelist[index].extend([1,1,0,0,0,0])
    elif(taste == "white-dry-and-nutty"):
        winelist[index].extend([1,1,0,0,0,1])
    index += 1

df['array'] = winelist

df.to_csv("winedata2.csv",sep=",", index=False)
# df.to_csv("winedata.csv",sep=",", index=False)