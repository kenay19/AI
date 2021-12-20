# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema:
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción:
Created on Fri Nov 19 18:48:29 2021
@author: omarl
"""

import pandas as pd
from matplotlib import pyplot as plt



class GraficaClases:
    
    def plot2D(self, X, Y,title):
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
        plt.title(title, 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})            
        nombreAtts = (X.columns)
        axs.set_xlabel(nombreAtts[0])
        axs.set_ylabel(nombreAtts[1])  
        axs.legend(clasesName)
        