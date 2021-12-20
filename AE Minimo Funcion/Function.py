# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que permite calcular la aptitud de los individuos
Created on Wed Dec  1 17:45:32 2021
@author: omarl
"""
class Function: 
    
    def fitness(self,individuo):
        '''
        Regresa la aptitud de un individuo

        Parameters
        ----------
        individuo : Individuo
            Dato que nos permite calcular su aptitud.
        Returns
        -------
        float
            aptitud del individuo .
        '''
        x, y = individuo.getPhenotype()
        return -((x-1.)**2 + (y+3)**2)