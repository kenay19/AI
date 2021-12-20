# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Primera versión de un AE

Soluciona el problema adivina contraseña

MECANISMO DE SELECCION 
Created on Fri Dec  3 22:22:34 2021
@author: omarl
"""

from Poblacion import Poblacion
from Individuo import Individuo
import numpy as np
import random 
class Seleccion:
    
    def seleccionaPadresIdx(self, poblacion, K=100):
        '''
        Selecciona los indices los padres con mejor aptitud de la poblacion
        Parameters
        ----------
        poblacion : int
            Poblacion en la que se buscara.
        K : int, optional
            Numero de padres a escoger. The default is 100.
        Returns
        -------
        list
            Lista con los indices de los mejores individuos en la poblacion.
        '''
        aptitudes = poblacion.fitnessPoblacion()
        idxWorst = poblacion.worst()
        aptitudes = np.array(aptitudes)
        div = aptitudes[idxWorst] 
        if div == 0:
            div = 1 
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        return random.choices(list(range(len(probs))), weights=probs, k=K)
    
    def seleccionaPadres(self, poblacion, K=100):
        '''
        Selecciona los padres para la siguiente generacion
        Parameters
        ----------
        poblacion : Poblacion
            Poblacion a elegir padres.
        K : int, optional
            Numero de padres a escoger. The default is 100.
        Returns
        -------
        padres : lista
            lista con los individuos listos a cruzar.

        '''
        idx = self.seleccionaPadresIdx(poblacion, K)
        padres = Poblacion(poblacion.ff, 1)
        ind = []
        for i in range(K):
            ind.append(poblacion.poblacion[idx[i]])
        padres.poblacion = ind
        return padres
    
    def seleccionNatural(self, poblacion, K=100):
        '''
        Selecciona a los mejores individuos para la siguiente Generacion
        Parameters
        ----------
        poblacion : Poblacion
            DESCRIPTION.
        K : int, optional
            Numero de los mejores individuos. The default is 100.
        Returns
        -------
        seleccionados : lista
            Mejores individuos para la siguiente generacion.

        '''
        idx = self.seleccionaPadresIdx(poblacion, K)
        seleccionados = Poblacion(poblacion.ff, 1)
        seleccionados.poblacion = []
        for i in range(K):
            genes = poblacion.poblacion[i].genes.copy()
            ind = Individuo()
            ind.genes = genes
            seleccionados.poblacion.append(ind)
        return seleccionados
            
        
        