# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema:
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción:
Created on Wed Nov 24 14:28:18 2021
@author: omarl
"""

import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as split
from sklearn.metrics import accuracy_score as accuracy
import sklearn.metrics as metrics
import sklearn.model_selection as ms
import numpy as np
data = pd.read_csv("diabetes.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]
xtrain,xtest,ytrain,ytest = split(X,Y,test_size=0.75,random_state=np.random.randint(0,1000))
maxK = int(np.ceil(np.sqrt(X.shape[0])))
ks = list(range(1,maxK))
param_grid = [
    {'n_neighbors':ks}        
]
knn = KNN()
clf = ms.GridSearchCV(knn,param_grid,scoring="accuracy",cv=20)
clf.fit(xtrain,ytrain)
print(clf.best_estimator_)
knn = KNN(3)
knn.fit(xtrain,ytrain)
ypred = knn.predict(xtest)
print("Acc: {:.4f}".format(np.sum(ypred==ytest)/len(ytest)))
print(accuracy(ytest,ypred))
print(metrics.classification_report(ytest,ypred))