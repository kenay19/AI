# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que permite la ejecucion del algoritmo evolutivo
Created on Wed Dec  1 18:25:12 2021
@author: omarl
"""
from Poblacion import Poblacion
from Individuo import Individuo
from Seleccion import Seleccion
from Function import Function
import numpy as np 
import random as r 
class AE:
    
    
    def __init__(self,POB=100,GENERACION=300):
        '''
        Genera una poblacion inicial y genera datos miembro
        Parameters
        ----------
        POB : int, optional
            Numero de individuos en una poblacion. The default is 100.
        GENERACION : int, optional
            Cantidad de nuevas generaciones. The default is 300.
        Returns
        -------
        None.

        '''
        self.generaciones = GENERACION
        self.poblacion = Poblacion(POB)
        self.sel = Seleccion()
        self.ff = Function()
        
    def evolve(self):
        '''
         Genera las nuevas generaciones y a su vez muestra al mejor individuo 

        Returns
        -------
        None.

        '''
        for generacion in range(self.generaciones):
            K = int(len(self.poblacion.poblacion)/2)
            padres = self.sel.seleccionaPadres(self.poblacion, K)
            madres = self.sel.seleccionaPadres(self.poblacion, K)
            descendencia = []
            for mama,papa in zip(madres.poblacion,padres.poblacion):
                hija,hijo = mama.cruza(papa)
                descendencia.append(hija)
                descendencia.append(hijo)
            hijos = Poblacion(1)
            hijos.poblacion = descendencia
            total = np.ceil(len(hijos.poblacion)*0.05)
            for i in range(int(total)):
                idx = r.randrange(0, len(hijos.poblacion))
                hijos.poblacion[idx].mutar()  
            nuevaGeneracion = []
            for ind in self.poblacion.poblacion:
                nuevaGeneracion.append(ind) # Padres/Madres
            for ind in hijos.poblacion:
                nuevaGeneracion.append(ind) # Hijos
            temp = Poblacion(1)
            temp.poblacion = nuevaGeneracion
            nuevaGeneracion = temp
            idxBest = nuevaGeneracion.best() # El mejor individuo hasta ahora
            sigGeneracion = Poblacion(1)
            sigGeneracion.poblacion = [] #Empieza vacía
            IndividuoDeElite = Individuo()
            IndividuoDeElite.genes = nuevaGeneracion.poblacion[idxBest].genes.copy()
            sigGeneracion.poblacion.append(IndividuoDeElite) # Elitismo
            # Seleccionar N-1 individuos, que estarán en la siguiente generación
            temp = self.sel.seleccionNatural(nuevaGeneracion, len(self.poblacion.poblacion)-1)
            for item in temp.poblacion:
                sigGeneracion.poblacion.append(item)
            # Imprimir el mejor individuo*
            idxBest = sigGeneracion.best() 
            print("========== Mejor solucion en la generacion: "+str(generacion+1)+" ==========")
            print(str(sigGeneracion.poblacion[idxBest])+" FITNESS = " + str(self.ff.fitness(sigGeneracion.poblacion[idxBest])))
            print("===========================================================")
            self.poblacion.poblacion = sigGeneracion.poblacion
    