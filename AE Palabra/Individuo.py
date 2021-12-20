# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Representación para el problema de permutaciones
"Adivina la contraseña"

Created on Fri Dec  3 22:18:19 2021
@author: omarl
"""

import random
import numpy as np
class Individuo:
    
    def __init__(self):
        '''
        Genera las variables para el funcionamiento del individuo
        Returns
        -------
        None.
        '''
        self.alfabeto = "abcdefghijklmnopqrstuvwxyz "
        # Alfabeto como una lista
        self.alfabetoList = [i for i in self.alfabeto]
        self.genes = []
        
    def inicializa(self, k=12):
        '''
        Inicializa al individuo

        Parameters
        ----------
        k : int, optional
            Tamaño de la cadena. The default is 12.
        Returns
        -------
        None.

        '''
        self.genes = random.choices(self.alfabetoList, k=k)
    
    def getPhenotype(self):
        '''
        Regresa el fenotipo del individuo
        Returns
        -------
        str
            Cadena del fenotipo.
        '''
        return self.__str__()
        
    def getGenotype(self):
        '''
        Regresa el genotipo del inviduo
        Returns
        -------
        str
           cadena del genotipo.
        '''
        return "[" + self.genes + "]"
    
    def __str__(self):
        cad = ""
        for c in self.genes:
            cad += c
        return cad
    
    # Mecanismos de variación
    def cruza(self, madre):
        '''
        Cruza 2 individuos
        Parameters
        ----------
        madre : Individuo
            Individuo con el cual se cruzara el padre.
        Returns
        -------
        list
            Nuevo individuo.
        '''
        mama = madre.genes
        papa = self.genes
        numGenes = len(papa)
        cp = int(numGenes/2) # Crosspoint
        genesHijo = mama[0:cp]
        genesHijo.extend(papa[cp:])
        genesHija = papa[0:cp]
        genesHija.extend(mama[cp:])
        hija = Individuo()
        hija.genes = genesHija
        hijo = Individuo()
        hijo.genes = genesHijo
        return [hija, hijo]
    
    def mutar(self):
        '''
        Remplaza caracteres del individuo
        Returns
        -------
        None.
        '''
        total = len(self.genes)
        idx = np.random.randint(0, total)  # Indice del caracter a cambiar
        nuevo = random.choice(self.alfabeto)
        self.genes[idx] = nuevo  # Se reemplaza