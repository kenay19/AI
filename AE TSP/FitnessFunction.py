# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Nos permite obtener la aptitud de un individuo en una poblacion 
Created on Wed Sep 15 19:12:49 2021
@author: omarl
"""
import collections 
import numpy as np
class FitnessFunction:
    invocaciones = 0
    
    def __init__(self, distancias, ciudades):
        self.distancias = distancias
        self.ciudades = ciudades
        
    def maximaDistancia(self):
        maxDist = -1
        for lista in self.distancias:
            for distancia in lista:
                if distancia > maxDist:
                    maxDist = distancia
        return maxDist
    
    def frecuencyTable(self, ind):
        return collections.Counter(ind.genes)
    
    def distance(self, cityA, cityB):
        iA = self.ciudades.index(cityA)
        iB = self.ciudades.index(cityB)
        indice0 = iA
        indice1 = iB
        if iA < iB:
            indice0 = iB
            indice1 = iA
        return self.distancias[indice0][indice1]
        
    
    def fitness(self, individuo):
        freqs = self.frecuencyTable(individuo)
        sum = 0
        for i in freqs:
            sum += np.abs(freqs[i] - 1)
        penalizacion = sum * self.maximaDistancia()
        temp = 0 
        for i in range(len(individuo.genes)):
            if i < len(individuo.genes)-1:
                temp += self.distance(individuo.genes[i], individuo.genes[i+1])
        return penalizacion + temp + self.distance(individuo.genes[0],individuo.genes[len(individuo.genes)-1])
            