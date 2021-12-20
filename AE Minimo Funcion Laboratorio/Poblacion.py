# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Permite crear una poblacion
Created on Wed Dec  1 23:36:57 2021
@author: omarl
"""

from Individuo import Individuo
from Function import Function
import numpy as np 
class Poblacion: 
    
    def __init__(self,Parametros):#Iniciamos una poblacion de x individuos de n variables  
        self.ff = Function()
        self.par = Parametros
        poblacion = []
        for i in range(Parametros[3]):
            i = Individuo(Parametros[0],Parametros[1],Parametros[2])
            poblacion.append(i)
        self.poblacion = poblacion #hacemos la poblacion como un dato miembro
    
    def __str__(self): #Nos da el fitness de todos los individuos de la poblacion
        cad = ""
        aptitudes = self.fitnessPoblacion(self.par[4],self.par[5],self.par[6])
        for ind, aptitud in zip(self.poblacion, aptitudes):
            cad=cad + str(ind) + " FITNESS =  " + str(aptitud) + "\n"
        return cad
        
    def fitnessPoblacion(self,a,b,c):#mide la aptitude de cada individuo        
        fp = []
        for i in self.poblacion:
            fp.append(self.ff.fitness(i,a,b,c))
        return fp
    
    def best(self,a,b,c):#Retorna el indice del mejor individuo en la 
        aptitudes = self.fitnessPoblacion(a,b,c)
        return aptitudes.index(np.min(aptitudes))
    
    def worst(self,a,b,c):#Retorna el indice del pero indiviudo en la poblacion
        aptitudes = self.fitnessPoblacion(a,b,c)
        return aptitudes.index(np.max(aptitudes))