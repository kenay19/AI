# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema:
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción:
Created on Fri Nov 12 22:56:10 2021
@author: omarl
"""

import numpy as np
class Kmeans:
        
    def chooseCentroids(self):
        indices = np.random.randint(0, len(self.X), size=self.K)
        self.centroids = [np.array(self.X.iloc[i, :]) for i in indices]
        
        '''centroids = []
        for i in indices:
            centroids.append(self.X.iloc[i, :])
        '''    
    
    def computeDistance(self, ci):
        '''
        Calcula las distancias desde el centroide ci a 
        todas las instancias en self.X

        Parameters
        ----------
        ci : arreglo np
            DESCRIPTION. Centroide ci

        Returns
        -------
        Lista con todas las distancias

        '''
        distances = []
        z = np.array(self.X)
        for x in z:
            distances.append(np.sqrt(np.sum(np.power(ci-x,2))))
        return distances
    
    def assignToCentroid(self, distancias):
        '''
        Asigna a cada instancia de self.X el centroid 
        más cercano

        Parameters
        ----------
        distancias : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.asignacion = []# ejemplo [0, 2, 4, 1, 0]# item valor entre 0 y K-1
        aux = []
        for i in  range(len(distancias)):
            for c in range(self.K) :
                aux.append(float(distancias[i][c]))
            self.asignacion.append(np.argmin(np.array(aux)))
            aux = []
    
    def computeDistances(self):
        distancias = []
        for ci in self.centroids:
            distancias.append(self.computeDistance(ci))
        return distancias
        
    def fit(self, X, K):
        self.K  = K
        self.X = X
        self.chooseCentroids()
        for i in range(10): # mejorar
            self.assignToCentroid(self.computeDistances())
    
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
        Xtest = Xtest.values
        a = self.computeDistance2(Xtest)
        self.assignToCentroid(a)
        return self.asignacion
    
    
    def computeDistance2(self,X):
        distancias = []
        aux = []
        for x in np.array(X):
            for c in self.centroids:
                aux.append(np.sqrt(np.sum(np.power(c-x,2))))
            distancias.append(aux)
            aux = []
        return distancias