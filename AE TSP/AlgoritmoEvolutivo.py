# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Nos permite implementar el algoritmo 
Created on Wed Sep 15 19:11:26 2021
@author: omarl
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction
import random
import numpy as np
class AlgoritmoEvolutivo:
    
    def __init__(self, ciudades,distancias, TAM_POB=100, GENERACIONES=300):
        self.GENERACIONES = GENERACIONES
        self.c = ciudades
        self.d = distancias
        self.poblacion = Poblacion(ciudades,distancias, TAM_POB)
        self.sel = Seleccion()
        self.ff = FitnessFunction(distancias, ciudades)

    def evolve(self, GEN=1):
        for gen in range(GEN):
            K = int(len(self.poblacion.poblacion)/2)
            padres = self.sel.seleccionaPadres(self.c,self.d,self.poblacion, K)
            madres = self.sel.seleccionaPadres(self.c,self.d,self.poblacion, K)
            descendencia = []
            for mama, papa in zip(madres.poblacion, padres.poblacion):
                hijo, hija = mama.cruza(papa)
                descendencia.append(hija)
                descendencia.append(hijo)
            hijos = Poblacion(self.c,self.d, 1)
            hijos.poblacion = descendencia
            totalMutar = np.ceil(len(hijos.poblacion)*0.05)
            for i in range(int(totalMutar)):
                idx = random.randrange(0, len(hijos.poblacion))
                hijos.poblacion[idx].mutar()            
            nuevaGeneracion = []
            for ind in self.poblacion.poblacion:
                nuevaGeneracion.append(ind)
            for ind in hijos.poblacion:
                nuevaGeneracion.append(ind) 
            temp = Poblacion(self.c,self.d, 1)
            temp.poblacion = nuevaGeneracion
            nuevaGeneracion = temp
            idxBest = nuevaGeneracion.best()
            sigGeneracion = Poblacion(self.c,self.d,1)
            sigGeneracion.poblacion = [] 
            IndividuoDeElite = Individuo(self.c)
            IndividuoDeElite.genes = nuevaGeneracion.poblacion[idxBest].genes.copy()
            sigGeneracion.poblacion.append(IndividuoDeElite)
            temp = self.sel.seleccionNatural(self.c,self.d,nuevaGeneracion, len(self.poblacion.poblacion)-1)
            for item in temp.poblacion:
                sigGeneracion.poblacion.append(item)
            print("================== La mejor solucion en la generacion: ",gen+1," ==================")
            idxBest = sigGeneracion.best()
            print(sigGeneracion.poblacion[idxBest]," Distancia: ",self.ff.fitness(sigGeneracion.poblacion[idxBest]))
            self.poblacion.poblacion = sigGeneracion.poblacion
