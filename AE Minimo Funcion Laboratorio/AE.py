# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Permite la ejecucion del algoritmo
Created on Thu Dec  2 13:45:29 2021
@author: omarl
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from Function import Function
from Graficas import Graficas
import random
import numpy as np
import os 
import imageio
from Graficas import Graficas

class AE:
    def __init__(self,PARAMETROS):
        self.GENERACIONES = PARAMETROS[7]
        self.poblacion = Poblacion(PARAMETROS)
        self.ff = Function()
        self.sel = Seleccion()
        self.par = PARAMETROS
        self.n = PARAMETROS[0]
        self.a = PARAMETROS[4]
        self.b = PARAMETROS[5]
        self.c = PARAMETROS[6]
        if self.n == 2:
            self.Graf = Graficas(PARAMETROS)
        self.names = []
        self.k  = 0 
        self.prueba = 0


    def evolve(self):
        for gen in range(self.GENERACIONES):
            K = int(len(self.poblacion.poblacion)/2)
            padres = self.sel.seleccionaPadres(self.par,self.n,self.a,self.b,self.c,self.poblacion, K)
            madres = self.sel.seleccionaPadres(self.par,self.n,self.a,self.b,self.c,self.poblacion, K)
            descendencia = []
            for mama, papa in zip(madres.poblacion, padres.poblacion):
                hijo, hija = papa.cross(mama,self.n)
                descendencia.append(hija)
                descendencia.append(hijo)
            # Mutar al 5% de la descendencia
            hijos = Poblacion(self.par)
            hijos.poblacion = descendencia
            # Calcula el 5% del tamaño de la población
            totalMutar = np.ceil(len(hijos.poblacion)*0.05)
            # Muta a algunos individuos seleccionados estocásticamente.
            # Seleccionar self.TAM_POB individuos (usar elitismo)
            for i in range(int(totalMutar)):
                idx = random.randrange(0, len(hijos.poblacion))
                hijos.poblacion[idx].mutar()  
            # Unir  padres/madres + hijos
            #self.poblacion.poblacion unir con hijos
            nuevaGeneracion = []
            for ind in self.poblacion.poblacion:
                nuevaGeneracion.append(ind) # Padres/Madres
            for ind in hijos.poblacion:
                nuevaGeneracion.append(ind) # Hijos
            temp = Poblacion(self.par)
            temp.poblacion = nuevaGeneracion
            nuevaGeneracion = temp

            # Seleccionar self.TAM_POB individuos (usar elitismo)
            # Mecanismo de elitismo
            idxBest = nuevaGeneracion.best(self.a,self.b,self.c) # El mejor individuo hasta ahora
            sigGeneracion = Poblacion(self.par)
            sigGeneracion.poblacion = [] #Empieza vacía
            IndividuoDeElite = Individuo(self.n)
            IndividuoDeElite.genes = nuevaGeneracion.poblacion[idxBest].genes.copy()
            sigGeneracion.poblacion.append(IndividuoDeElite) # Elitismo
            # Seleccionar N-1 individuos, que estarán en la siguiente generación
            temp = self.sel.seleccionNatural(self.par,self.n,self.a,self.b,self.c,nuevaGeneracion, len(self.poblacion.poblacion)-1)
            for item in temp.poblacion:
                sigGeneracion.poblacion.append(item)
            # Imprimir el mejor individuo*
            print("================= Mejor solucion en la generacion ",gen+1," =================")
            idxBest = sigGeneracion.best(self.a,self.b,self.c) # El mejor individuo hasta ahora
            print(sigGeneracion.poblacion[idxBest], "f(xn) = ",self.ff.fitness(sigGeneracion.poblacion[idxBest],self.a,self.b,self.c))
            self.poblacion.poblacion = sigGeneracion.poblacion
            if self.n == 2:
                self.Graf.grafica(gen,sigGeneracion.poblacion[idxBest],self.a,self.b,self.c)
                self.names.append(str(gen)+".png")
            if self.prueba == sigGeneracion.poblacion[idxBest]:
                self.k +=1 
                if self.k == 5:
                    return
            else:
                self.prueba = sigGeneracion.poblacion[idxBest]
                self.k = 0
        if self.n == 2:
            with imageio.get_writer('mygif.gif', mode='I') as writer:
                for filename in self.names:
                    image = imageio.imread(filename)
                    writer.append_data(image)
        
            # Remove files
            for filename in set(self.names):
                os.remove(filename)