# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que permite la creacion de la poblacion
Created on Wed Dec  1 17:24:06 2021
@author: omarl
"""
from Individuo import Individuo
from Function import Function
import numpy as np 
class Poblacion:
    
    def __init__(self, TAM_POB=100):
        '''
        Inicia un poblacion con n individuos
        Parameters
        ----------
        TAM_POB : int
            Da el numero de individuos en la povlacion
        Returns
        -------
        None.
        '''
        self.ff = Function()
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo()
            poblacion.append(i)
        self.poblacion = poblacion    
    
    def __str__(self):
        '''
        Pone todos los datos del individuo
        Returns
        -------
        cad : str
            Cadena con los datos de cada individuo
            en la poblacion.
        '''
        cad =""
        aptitudes = self.fitnessPoblacion()
        for individuo,aptitud in zip( self.poblacion,aptitudes):
            cad = cad + str(individuo)+" FTINESS "  +str(aptitud) +"\n"
        return cad 
    
    def fitnessPoblacion(self):
        '''
        Calcula la aptitud de cada individuo en la poblavcion

        Returns
        -------
        fp : list
            Lista con todas las aptitudes de la poblacion.

        '''
        fp = []
        for ind in self.poblacion:
            fp.append(self.ff.fitness(ind))
        return fp
    
    def best(self):
        '''
        Determina el indice del individuo mas apto en la poblacion

        Returns
        -------
        int
            Indice del mejor individuo.

        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.max(aptitudes))# Por que es negativo
    
    def worst(self):
        '''
        Regresa el indice del peor individuo de la poblacion
        Returns
        -------
        int
            Indice del peor individuo.
        '''
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.min(aptitudes))