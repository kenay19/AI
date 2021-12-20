# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que permite crear un individuo 
Created on Wed Dec  1 22:48:16 2021
@author: omarl
"""

import random as r

class Individuo:
    
    def __init__(self,K=1,bits = 8,intervalo = 1):
        '''
        Genera las variables necesarias para el funcionamiento del individuo
        Parameters
        ----------
        K : int, optional
            Numero de variables del individuo. The default is 1.
        bits : TYPE, optional
            Numero de bits por variable del individuo. The default is 8.
        intervalo : TYPE, optional
            Intervalo en el cual se encontraran los individuos . The default is 1.
        Returns
        -------
        None.
        '''
        self.k = K
        self.bits = bits
        self.inte = intervalo
        self.genes = r.choices([0,1],k=bits*K)
    
    def intervalo(self,k):
        '''
        Regresa la suma de los valoes de los bits
        Parameters
        ----------
        k : int
            Numero de bits.
        Returns
        -------
        result : int
            Suma de los bits.
        '''
        result = 0
        for i in range(k):
            result += 2**i
        return result
    
    def getPhenotype(self):
        '''
        Obtiene el fenotipo del individuo
        Returns
        -------
        lista : list
            Devuelve la lista con n variables por individuos .
        '''
        lista = [] 
        quitar = ["[","]",","," "]
        for i in range(self.k):
            lista.append(self.genes[self.bits*i:self.bits*(i+1)])
            if lista[i][0] == 0:
                signo = 1
            else:
                signo = -1
            lista[i] = str(lista[i]) 
            for signoa in quitar:
                lista[i] = lista[i].replace(signoa,"")
            lista[i] = int(lista[i][1:],2) * signo * self.inte/self.intervalo(len(lista[i]))
        return lista
    
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
    
    def __str__(self):# Nos da el fenotipo y el genotipo
        variables = self.getPhenotype() 
        cad = self.getGenotype() +" -> " #Obtnemos el genotipo del individuo
        for i in range(len(variables)): #Concatenamos el fenotipo del individuo variable por variable
            if i < len(variables)-1:
                cad += str(variables[i]) + ", "
            elif i == len(variables) -1:
                cad += str(variables[i])
        return  cad 
    
    #Metodo de Cruza
    def cross(self,madre,k):
        '''
        Cruza dos padres 
        Parameters
        ----------
        madre : Individuo
            Individuo con el que padre se cruzara .
        k : int
            Numero de bits por individuo.
        Returns
        -------
        obj1 : Individuo
            Hijo de la cruza.
        obj2 : Individuo
            Hija de la cruza

        '''
        #Tomamos los genes del padre y de la madre 
        mama = madre.genes
        papa = self.genes
        #"Partimos" al padre y la madre en tres
        hijo = papa[0:int(len(papa)/3)] #Agremos el primer tercio del padre al hijo
        hijo.extend(mama[int(len(mama)/3):2*int(len(mama)/3)])#Agremos el segundo tercio de la madre al hijo
        hijo.extend(papa[2*int(len(papa)/3):])#Agremos el ultimo tercio del padre al hijo
        hija = mama[0:int(len(mama)/3)]#Agremos el primer tercio de la madre a la hija
        hija.extend(papa[int(len(papa)/3):2*int(len(papa)/3)])#Agremos el segundo tercio del padre a la hija
        hija.extend(mama[2*int(len(mama)/3):])#Agremos el ultimo tercio de la madre a la hija
        #Hacemos a los hijos individuos
        obj1 = Individuo(k)
        obj2 = Individuo(k)
        obj1.genes = hijo
        obj2.genes = hija
        #Los Retornamos en una lista
        return obj1,obj2
    
    #Cambiamos a todo el individuo
    def mutar(self):
        '''
        Se modifica todo el individuo
        Returns
        -------
        None.
        '''
        self.genes = r.choices([0,1],k=len(self.genes))