# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Permite obtener la aptitud de cada indivduo
Created on Wed Dec  1 23:38:31 2021
@author: omarl
"""
import numpy as np

class Function:
    def fitness(self,individuo,a,b,c): #Devuelve el valor de la funcion para cada individuo que lo tomaremos como su actitud
        
        x = individuo.getPhenotype()
        return -((a*np.exp(-b*np.sqrt((1/(len(x)-1))*self.suma(x,len(x)-1))))-np.exp((1/(len(x)-1))*self.cos(x,c,len(x)-1))+a+np.exp(1))
    
    def suma(self,x,n):#Suma de manera recursiva cada variable elevada al cuadrado
        if n == 0:
            return x[0]**2
        else:
            return x[n]**2 + self.suma(x,n-1)

    def cos(self,x,c,n):#Suma recursivamente el coseno de cada variable multiplicada por una constante c 
        if n == 0:
            return np.cos(c*x[0])
        else:
            return np.cos(c*x[n])+self.cos(x,c,n-1)
        
    def fitnessGraf(self,x,a,b,c): #Devuelve el valor de la funcion para cada individuo que lo tomaremos como su actitud
        return -((a*np.exp(-b*np.sqrt((1/(len(x)-1))*self.suma(x,len(x)-1))))-np.exp((1/(len(x)-1))*self.cos(x,c,len(x)-1))+a+np.exp(1))