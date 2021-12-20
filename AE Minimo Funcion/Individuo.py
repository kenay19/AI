# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos 
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que crea al individuo asi como sus metodos para su funcionamiento
Created on Wed Dec  1 16:42:01 2021
@author: omarl
"""
import random as r 
class Individuo:
    
    def __init__(self,K=16):
        '''
        Inicializamos el individuo con una cadena de k bits
        Parameters
        ----------
        k : int
            Numero de bits por individuo
            Por defecto el individuo tendra k bits
        Returns
        -------
        None.
        '''
        self.genes = r.choices([0,1],k=K)
    
    def getPhenotype(self):
        '''
        Regresa el valor del individuo en base 10
        Returns
        -------
        list
            Regresa en una lista dichos valores 
            X,Y
        '''
        quitar = ["[","]",","," "]
        x = self.genes[0:8]
        y = self.genes[8:]
        if x[0] == 0:
            signoX = +1
        else:
            signoX = -1
        if y[0] == 0:
            signoY = +1
        else:
            signoY = -1
        x = str(x[1:])
        y = str(y[1:])
        for signo in quitar:
            x = x.replace(signo,'')
            y = y.replace(signo,'')
        return [int(x, 2)*signoX*5./127.,int(y, 2)*signoY*5./127.]
    
    def getGenotype(self):
        '''
        Regresa una str con cada elemento del individuo en base 2
        Returns
        -------
        STR
            Cadena con los elementos del individuo

        '''
        individuo = self.genes
        individuo = str(individuo)
        quitar = ["[","]",","," "]
        for signo in quitar:
            individuo = individuo.replace(signo,'')
        return individuo
    
    def __str__(self):
        '''
        Regresa una cadena con el genotupo y fenotipo del Individuo
        Returns
        -------
        str
           fenotipo y genotipo del individuo

        '''
        x, y = self.getPhenotype()
        return self.getGenotype() + " -> " + "x = {:.4f}, y = {:.4f}".format(x,y)
    
   
    def cruza(self, madre):
        '''
        Toma dos individuos y cruza sus genes
        Parameters
        ----------
        madre : Individuo
            Es el individuo que tiene los genes de la madre
        Returns
        -------
        list
            Lista que contiene dos hijos.

        '''
        mama = madre.genes
        papa = self.genes
        hijo = papa[0:8]
        hijo.extend(mama[8:])
        hija = mama[0:8]
        hija.extend(papa[8:])
        #En este momento los hijos son listas, no Individuos
        hijaObj = Individuo()
        hijaObj.genes = hija
        hijoObj = Individuo()
        hijoObj.genes = hijo
        return [hijaObj, hijoObj]
        
    
    def mutar(self):
        '''
        Modifica todos los genes del individuo 
        Returns
        -------
        None.

        '''
        self.genes = r.choices([0, 1], k=len(self.genes))