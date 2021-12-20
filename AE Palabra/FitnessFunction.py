# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción:Función de aptitud para el problema de adivina contraseña
Regresa el número de coincidencias entre el objetivo y el individuo.
Futuro: Regresa la posición de las coindicencias
Created on Fri Dec  3 22:17:40 2021
@author: omarl
"""

class FitnessFunction:
    invocaciones = 0 #Variables de clase
    
    def __init__(self, objetivo):
        '''
        Carga en la funcion la palabra a adivinar
        Parameters
        ----------
        objetivo : str
            cadena la cual adivinaremos.
        Returns
        -------
        None.
        '''
        self.objetivo = objetivo
        
    def fitness(self, individuo):
        '''
        Toma al individuo y verifica el numero de caracteres iguales a la funcion objetivo
        Parameters
        ----------
        individuo : Individuo
            Comparacion con la funcion objetivo.
        Returns
        -------
        coincidencias : int
            Numero de coicidencias del individuo y el funcion objetivo.
        '''
        FitnessFunction.invocaciones +=1 
        coincidencias = 0
        i = 0
        for letra in individuo.genes:
            if self.objetivo[i] == letra:
                coincidencias += 1
            i += 1
        return coincidencias