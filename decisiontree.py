# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:06:58 2020

@author: acer
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
df= pd.read_csv("balance-scale.csv")
x=df.iloc[:,1:]
y=df.iloc[:,0]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=0)
print(xtrain.shape,xtest.shape)
gini=DecisionTreeClassifier(criterion='gini',max_depth=3,min_samples_leaf=5)
gini.fit(xtrain,ytrain)
pre=gini.predict(xtest)
print(pre)