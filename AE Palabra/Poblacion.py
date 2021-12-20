# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción:Soluciona el adivina contraseña

POBLACION
Created on Fri Dec  3 22:19:03 2021
@author: omarl
"""

from Individuo import Individuo
from FitnessFunction import FitnessFunction
import numpy as np

class Poblacion:
    
    def __init__(self, ff, TAM_POB=100):
        '''
        Genera las variables necesarias para el funcionamiento de la poblacion
        Parameters
        ----------
        ff : FitnessFunction
            DESCRIPTION.
        TAM_POB : int, optional
            Tamaño de la poblacion. The default is 100.
        Returns
        -------
        None.
        '''
        self.ff = ff
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo()
            i.inicializa(k=len(self.ff.objetivo))
            poblacion.append(i)
        self.poblacion = poblacion    
    
    def __str__(self):
        cad = ""
        aptitudes = self.fitnessPoblacion()
        for ind, aptitud in zip(self.poblacion, aptitudes):
            cad=cad + str(ind) + " FITNESS =  " + str(aptitud) + "\n"
        return cad
    
    def fitnessPoblacion(self):
        '''
        Calcula las aptitudes de los individuos 
        Returns
        -------
        fp : list
            lista con las aptitudes.
        '''
        fp = []
        for ind in self.poblacion:
            fp.append(self.ff.fitness(ind))
        return fp
            
    #Elitismo: identificar al mejor individuo de una poblacion
    def best(self):
        '''
        Regresa al mejor de la poblacion
        Returns
        -------
        int
           Indice del mejor de la poblacion.
        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.max(aptitudes)) # 
    
    def worst(self):
        '''
        Regresa el peor individuo
        Returns
        -------
        int
           Mejor individuo de la poblacion.
        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.min(aptitudes))# 