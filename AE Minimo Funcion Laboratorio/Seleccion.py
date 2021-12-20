# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que selecciona a los padres asi como los individuos para la siguiente generacion
Created on Thu Dec  2 13:44:34 2021
@author: omarl
"""

from Poblacion import Poblacion
from Individuo import Individuo
import numpy as np
import random
class Seleccion:
    
    def seleccionaPadresIdx(self,a,b,c,poblacion, K=100):
        '''
        Retorna los indices de los mejores individuos en la poblacion        
        Parameters
        ----------
        a : int
            parametro para la funcion de aptitud.
        b : int
            parametro para la funcion de aptitud.
        c : int
            parametro para la funcion de aptitud.
        poblacion : Poblacion
            Poblacion en la cual buscar a los mejores individuos.
        K : int, optional
            Numero de individuos a seleccionar dentro de la poblacion. The default is 100.
        Returns
        -------
        list
            Lista con los indices de los mejores individuos.
        '''
        aptitudes = poblacion.fitnessPoblacion(a,b,c)# Obtnemos las aptitudes de la poblacion
        idxWorst = poblacion.worst(a,b,c)#Es el valor mayor
        #Normalizamos las aptitudes
        aptitudes = np.array(aptitudes)
        aptitudes = 1.-aptitudes/aptitudes[idxWorst]
        #Convertir en probabilidades
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        #Eleige K padres
        return random.choices(list(range(len(probs))),weights=probs,k=K)
    
    def seleccionaPadres(self,par, n,a,b,c,poblacion, K=100):
        '''
        Busca los k padres para crear la descendencia
        Parameters
        ----------
        par : list
            parametros.
        n : int
            numero de variables en el individuo.
        a : int
            parametro para la funcion de aptitud.
        b : int
            parametro para la funcion de aptitud.
        c : int
            parametro para la funcion de aptitud.
        poblacion : Poblacion
            Poblacion a escoger.
        K : int, optional
            numero de individuos a seleccionar. The default is 100.
        Returns
        -------
        padres : list
            lista de padres seleccionados.
        '''
        idx = self.seleccionaPadresIdx(a,b,c,poblacion,K)
        padres = Poblacion(par)
        ind = []
        for i  in range(K):
            ind.append(poblacion.poblacion[idx[i]])
        padres.poblacion = ind
        return padres
        
    
    def seleccionNatural(self,par,n,a,b,c,poblacion, K=100):
        '''
        Busca los k mejores individuos para la siguiente generacion
        Parameters
        ----------
        par : list
            parametros.
        n : int
            numero de variables en el individuo.
        a : int
            parametro para la funcion de aptitud.
        b : int
            parametro para la funcion de aptitud.
        c : int
            parametro para la funcion de aptitud.
        poblacion : Poblacion
            Poblacion a escoger.
        K : int, optional
            numero de individuos a seleccionar. The default is 100.
        Returns
        -------
        seleccionados : list
            lista de individuos seleccionados.
        '''
        seleccionados = Poblacion(par)
        seleccionados.poblacion = []
        for i in range(K):
            genes = poblacion.poblacion[i].genes.copy()
            ind = Individuo(n)
            ind.genes = genes
            seleccionados.poblacion.append(ind)
        return seleccionados