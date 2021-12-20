# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema:  Proyecto
Alumnos: Ernesto Martinez Islas, Fernando Emanuel Santacruz Lara y Kevin Omar Lazaro Ortega 
Profesor: Dr. Asdrúbal López Chau
Descripcion: Algoritmo KNN el cual nos clasificara los productos 
Created on Fri Nov 19 18:55:11 2021
@author: omarl
"""

import numpy as np
class MyKNN:
    
    def fit(self, X, Y, K=5):
        '''
        Genera o calibra el modelo con los datos

        Parameters
        ----------
        X : DataFrame
            DESCRIPTION. Atributos del conjunto de datos
                        de entrenamiento
        Y : Series
            DESCRIPTION. Etiquetas del conjunto de datos
                        de entrenamiento

        Returns
        -------
        None.

        '''
        self.X = X
        self.Y = Y
        self.K = K

    
    def calculaDistancias(self, xi):
        '''
        Calcula la distancia entre xi y todas las instancias en self.X

        Parameters
        ----------
        xi : array numpy
            DESCRIPTION.

        Returns
        -------
        List
            DESCRIPTION. Todas las distancias en una lista

        '''
        X = self.X.values # Como arreglo de numpy
        distancias = []
        for xj in X:
            d = self.distanciaEuclideana(xi, xj)
            distancias.append(d)
        return distancias
        
    
    def distanciaEuclideana(self, xi, xj):
        '''
        Calcula distancia Euclideana entre
        dos instancias

        Parameters
        ----------
        xi : array numpy
            DESCRIPTION. Instancia i
        xj : array numpy
            DESCRIPTION. Instancia j

        Returns
        -------
        float
            DESCRIPTION. Distancia Euclideana
                    entre xi y xj

        '''
        return np.sqrt(np.sum(np.power(xi - xj, 2)))

    def getIndicesKDistanciasMenores(self, distancias):
        indices = []
        for k in range(self.K):
            idx = distancias.index( np.min(distancias) )
            distancias[idx] = np.max(distancias)
            indices.append(idx)
        return indices
    
    def calcularClaseMasFrecuente(self, indices):
        KClases = [self.Y[i] for i in indices]
        conjunto = list(set(KClases))
        frecuencia = [KClases.count(i) for i in conjunto]
        idx = np.argmax(frecuencia)
        return conjunto[idx]

    def predict(self, Xtest):
        '''
        Realiza la prediccion con K-NN

        Parameters
        ----------
        Xtest : DataFrame o array numpy
            DESCRIPTION. Atributos de instancias 

        Returns
        -------
        ypred : List
            DESCRIPTION. Las predicciones 

        '''
        ypred = []
        Xtest = Xtest.values
        for xi in Xtest:
            distancias = self.calculaDistancias(xi)
            indices = self.getIndicesKDistanciasMenores(distancias)
            ypred.append(self.calcularClaseMasFrecuente(indices))
        return ypred