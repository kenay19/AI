#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Machine Learning
Alumno: Tu Nombre
Profesor: Dr. Asdrúbal López Chau
Descripción: Graficar los datos de un conjunto etiquetado

Created on Mon Sep 27 14:13:57 2021

@author: asdruballopezchau
"""

import pandas as pd
from matplotlib import pyplot as plt

# Leer los datos 
datos = pd.read_csv("../data/iris.csv")
# Seleccionamos las dos primeras dimensiones
X = datos.iloc[:, 0:2]
# Seleccionamos las clases
Y = datos.iloc[:, -1]

class GraficaClases:
    
    def plot2D(self, X, Y):
        """
        Grafica las clases en un conjunto de datos etiquetado
        con dos atributos
        Parameters
        ----------
        X : DataFrame
            Contiene los atributos.
        Y : Series pandas
            Contiene las etiquetas o clases.

        Returns
        -------
        None.
        """
        colores = ['or', 'sg', 'hb', '*y']
        clases = list(set(Y))
        fig, axs = plt.subplots(1)
        clasesName = []
        for i in range(len(clases)):
            x = X.loc[Y == clases[i]].iloc[:, 0]
            y = X.loc[Y == clases[i]].iloc[:, 1]
            axs.plot(x, y, colores[i])
            clasesName.append(clases[i])
            
        nombreAtts = (X.columns)
        axs.set_xlabel(nombreAtts[0])
        axs.set_ylabel(nombreAtts[1])  
        axs.legend(clasesName)
        
gc = GraficaClases()
gc.plot2D(X, Y)
