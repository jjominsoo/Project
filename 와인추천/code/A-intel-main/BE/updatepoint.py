import pandas as pd
import numpy as np
import json

df = pd.read_csv("BE/winedata3.csv")
with open("BE/rate.json","r") as json_file:
    update = json.load(json_file)

print(update[0]['index'])


for wine in range(len(update)):
    df['points'][update[wine]['index']] += update[wine]['rate']
    print(df['points'][update[wine]['index']])
        
df.to_csv("BE/winedata3.csv",sep=",", index=False)