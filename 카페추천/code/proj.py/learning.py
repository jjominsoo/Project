import pandas as pd
import numpy as np
import random as rnd

# import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings(action='ignore')

df = pd.read_excel('proj.py\integrated_rmdup_process_complete.xlsx')
test_df = pd.read_excel('proj.py\\test.xlsx')

data = df
# print(data)
X_train = df.drop("열1",axis=1)
# Y_train = df["열1"]
# X_test = test_df.drop("열1",axis=1).copy()

# print(similarity_cafe)
similarity_cafe = cosine_similarity(X_train,X_train).argsort()[:,::-1]

def recommend_cafe_list(df,cafe,top=80):
    target_cafe_index = df[df['열1'] == cafe].index.values
    sim_index = similarity_cafe[target_cafe_index,:top].reshape(-1)
    sim_index = sim_index[sim_index!=target_cafe_index]
    result = df.iloc[sim_index].sort_values('coffee',ascending=False)[:5]
    print(result)
    return result

recommend_cafe_list(data,cafe='서촌금상고로케')

# logreg = LogisticRegression()
# logreg.fit(X_train, Y_train)
# Y_pred = logreg.predict(X_test)
# acc_log = round(logreg.score(X_train, Y_train) * 100, 2)
# print(acc_log)

# X_test = 