# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema:  Proyecto
Alumnos: Ernesto Martinez Islas, Fernando Emanuel Santacruz Lara y Kevin Omar Lazaro Ortega 
Profesor: Dr. Asdrúbal López Chau
Descripción: Pruebas
Created on Fri Nov 12 20:35:00 2021
@author: omarl
"""

import pymysql  as sql
import pandas as pd
from Tratamiento import Tratamiento 
from GraficaClases import GraficaClases
import random
from MyKNN import MyKNN
con = sql.connect(host = 'localhost',user = 'root', password = '', db = 'Abarrotes')
opcion = "S"
aux = Tratamiento(con)
gc = GraficaClases()
while(opcion=="S" or opcion=="s"):
    opcion = input("Desea Nuevos Datos? S/N: ")
    if(opcion == "S" or opcion=="s"):
        aux.writeDocummet(aux.tratamientoDatos(),"datos.csv")
        datos = pd.read_csv("datos.csv")
        X = datos.iloc[:, 2:4]
        Y = datos.iloc[:, -1]
        gc.plot2D(X, Y,"Datos Entrenamiento") 
    elif(opcion == "N" or opcion=="n"):
        datos = pd.read_csv("datos.csv")
        X = datos.iloc[:, 2:4]
        Y = datos.iloc[:, -1]
        idx = list(range(X.shape[0]))
        random.shuffle(idx) 
        Xtr = pd.DataFrame(columns=X.columns)
        Ytr = []
        for i in range(int(len(idx)*.66)):
            Xtr = Xtr.append(X.iloc[idx[i], :])
            Ytr.append(Y[idx[i]])
        Xtest = pd.read_csv("prueba.csv")
        clf = MyKNN()
        k=int(input("Numero de Vecinos: "))
        clf.fit(Xtr, Ytr, K=k)
        p = pd.DataFrame()
        ypred = clf.predict(Xtest.iloc[:,1:3])
        p["Productos"] = Xtest.iloc[:,0]
        p["Cantidad"] = Xtest["Cantidad"]
        p["Venta"] = Xtest["Venta"]
        p["Etiquetas"] = ypred
        y = p.iloc[:,-1]
        x = p.iloc[:,1:3]
        gc.plot2D(x,y,"Con " +str(k) +" Vecinos") 
        aux.writeDocummet(p,"clasificados.csv")
    opcion = input("Desea Continuar? S/N: ")