# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Genera un poblacion de individuos para este problema
Created on Wed Sep 15 19:10:52 2021
@author: omarl
"""

from Individuo import Individuo
from FitnessFunction import FitnessFunction
import numpy as np

class Poblacion:
    
    def __init__(self,ciudades,distancias, TAM_POB=100):
        '''
        Genera los datos para el funcionamiento de la poblacion
        Parameters
        ----------
        ciudades : List
            Nombres de las ciudades.
        distancias : list
            lista con las distancias de cada ciudad a cada ciudad.
        TAM_POB : int, optional
            Numero de individuo por poblacion. The default is 100.
        Returns
        -------
        None.
        '''
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo(ciudades)
            i.inicializa()
            poblacion.append(i)
        self.poblacion = poblacion    
        self.ff = FitnessFunction(distancias, ciudades)
    
    def __str__(self):
        cad = ""
        aptitudes = self.fitnessPoblacion()
        for ind, aptitud in zip(self.poblacion, aptitudes):
            cad=cad + str(ind) + " FITNESS =  " + str(aptitud) + "\n"
        return cad
    
    def fitnessPoblacion(self):
        '''
        Obtiene la aptitud de cada individuo en la poblacion
        Returns
        -------
        fp : list
            Lista con las aptitudes de todos los individuos en la poblacion.
        '''
        fp = []
        for ind in self.poblacion:
            fp.append(self.ff.fitness(ind))
        return fp
            
    def best(self):
        '''
        Obtiene al mejor individuo en la poblacion
        Returns
        -------
        int
           Indice del mejor individuo en la poblacion .
        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.min(aptitudes))
    
    def worst(self):
        '''
        Obtiene al peor individuo en la poblacion
        Returns
        -------
        int
            Indice del peor individuo en la poblacion.
        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.max(aptitudes))#