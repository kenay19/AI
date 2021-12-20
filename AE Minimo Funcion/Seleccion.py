# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que permite la seleccion de los padres asi como los mejores individuos 
para la siguiente generacion 
Created on Wed Dec  1 18:37:38 2021
@author: omarl
"""

from Poblacion import Poblacion
from Individuo import Individuo
import numpy as np
import random 
class Seleccion:
    
    def seleccionaPadresIdx(self, poblacion, K=100):
        '''
        Regresa una lista de los indices de los mejores individuos
        Parameters
        ----------
        poblacion : Poblacion
            Toma todos los individuos con los que se esta trabajando.
        K : int, optional
            Toma una cantidad k de individuos mejores que el resto de la poblacion. The default is 100.

        Returns
        -------
        list
            Lista con los k individuos mejores en la poblacion.
        '''
        aptitudes = poblacion.fitnessPoblacion()
        idxWorst = poblacion.worst()# Valor mayor
        # Normalizar las aptitudes
        aptitudes = np.array(aptitudes)
        aptitudes = 1.-aptitudes/aptitudes[idxWorst]
        #Convierte las aptitudes en probabilidades usando softmax
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        #Elige K padres/madres
        return random.choices(list(range(len(probs))), weights=probs, k=K)
    
    def seleccionaPadres(self, poblacion, K=100):
        '''
        Genera los padres de la siguiente generacion
        Parameters
        ----------
        poblacion : Poblacion
            Toma una poblacion para elegir los padres.
        K : int, optional
            cantidad de padres. The default is 100.
        Returns
        -------
        padres : list
            Lista de padres.
        '''
        idx = self.seleccionaPadresIdx(poblacion, K)
        padres = Poblacion(1)
        ind = []
        for i in range(K):
            ind.append(poblacion.poblacion[idx[i]])
        padres.poblacion = ind
        return padres
    
    def seleccionNatural(self, poblacion, K=100):
        '''
        Selecciona a los k individuos mejores entre los hijos y los padres para la nueva generacion
        Parameters
        ----------
        poblacion : Poblacion
            Conjunto de padres e hijos .
        K : int, optional
            Tamaño de la nueva poblacion. The default is 100.
        Returns
        -------
        seleccionados : Poblacion
            Siguiente Generacion.
        '''
        seleccionados = Poblacion(1)
        seleccionados.poblacion = []
        for i in range(K):
            genes = poblacion.poblacion[i].genes.copy()
            ind = Individuo()
            ind.genes = genes
            seleccionados.poblacion.append(ind)
        return seleccionados