# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Machine Learnig
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Ejecucion del codigo
Created on Fri Dec  3 22:22:59 2021
@author: omarl
"""

import numpy as np
import pandas as pd
from MyKNN import MyKNN
import random
ejecucion = []
for u in range(10):
    datos = pd.read_csv("iris.csv")
    X = datos.iloc[:, 0:-1] # Atributos
    Y = datos.iloc[:, -1]   # Etiquetas
    # Revolver los indices
    idx = list(range(X.shape[0]))
    random.shuffle(idx) 
    #  Training set (selección pseudo-aleatoria)
    #  66% para entrenamiento
    Xtr = pd.DataFrame(columns=X.columns)
    Ytr = []
    for i in range(int(len(idx)*.66)):
        Xtr = Xtr.append(X.iloc[idx[i], :])
        Ytr.append(Y[idx[i]])
    #  Test set
    Xtest = pd.DataFrame(columns=X.columns)
    Ytest = []
    for i in range(int(len(idx)*.66), len(idx)):
        Xtest = Xtest.append(X.iloc[idx[i], :])
        Ytest.append(Y[idx[i]])
    clf = MyKNN()
    clf.fit(Xtr, Ytr, K=3)
    ypred = clf.predict(Xtest)
    #medir que tambien predice las etiquetas
    suma = np.sum(np.array(Ytest)==np.array(ypred))
    accuracy = suma/len(Ytest)
    ejecucion.append(accuracy)        
prom = np.sum(np.array(ejecucion))/len(ejecucion)
des = np.std(ejecucion)
print("Promedio: ",prom)
print("Desviacion: ",des )

