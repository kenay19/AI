# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Nos permite seleccionar los padres de la siguiente generacion
Created on Wed Sep 15 19:13:20 2021
@author: omarl
"""

from Poblacion import Poblacion
from Individuo import Individuo
import numpy as np
import random 
class Seleccion:
    
    def seleccionaPadresIdx(self, poblacion, K=100):
        aptitudes = poblacion.fitnessPoblacion()
        idxWorst = poblacion.worst()
        aptitudes = np.array(aptitudes)
        div = aptitudes[idxWorst] 
        if div == 0:
            div = 1            
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        return random.choices(list(range(len(probs))), weights=probs, k=K)
    
    def seleccionaPadres(self, ciudades,distancias,poblacion, K=100):
        idx = self.seleccionaPadresIdx(poblacion, K)
        padres = Poblacion(ciudades,distancias, 1)
        ind = []
        for i in range(K):
            ind.append(poblacion.poblacion[idx[i]])
        padres.poblacion = ind
        return padres
    
    def seleccionNatural(self, ciudades,distancias,poblacion, K=100):
        seleccionados = Poblacion(ciudades,distancias, 1)
        seleccionados.poblacion = []
        for i in range(K):
            genes = poblacion.poblacion[i].genes.copy()
            ind = Individuo(ciudades)
            ind.genes = genes
            seleccionados.poblacion.append(ind)
        return seleccionados
            