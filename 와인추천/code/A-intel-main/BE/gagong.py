import pandas as pd

taste_lb=50
taste_st=50
taste_ds=50
taste_sa=50

df = pd.read_csv("winedata.csv")

df.insert(10,'LightBold',taste_lb)
df.insert(11,'SmoothTannin',taste_st)
df.insert(12,'DrySweet',taste_ds)
df.insert(13,'SoftAcidic',taste_sa)

for wine in df['title']:
    newstring = ''.join([i for i in wine if not i.isdigit()])
    newstring = newstring.replace(" ","+" )
    newstring = newstring.replace("(","" )
    newstring = newstring.replace(")","" )

    df['title'] = df['title'].replace(wine, newstring)

df.to_csv("winedata.csv",sep=",", index=False)
print(df['title'])
# df.to_csv("winedata.csv",sep=",", index=False)