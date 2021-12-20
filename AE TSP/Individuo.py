# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Describimos la clase individuo
Created on Wed Sep 15 19:10:36 2021
@author: omarl
"""

import random
class Individuo:
       
    def __init__(self, listaCiudades):
        '''
        Genera las variables para usar correctamente al individuo
        Parameters
        ----------
        listaCiudades : list
            Lista de las ciudades.
        Returns
        -------
        None.
        '''
        self.ciudades = listaCiudades
        self.genes = []
        
    def inicializa(self):
        '''
        Genera los genes del individuo
        Returns
        -------
        None.
        '''
        numCiudades = len(self.ciudades)
        self.genes = random.sample(self.ciudades, numCiudades)

    def getPhenotype(self):
        '''
        Obtiene el fenotipo del individuo
        Returns
        -------
        genes
            Genes del individup.
        '''
        return self.genes
        
    def getGenotype(self):
        '''
        Obtiene el genotipo del individuo
        Returns
        -------
        ruta : str
            Cadena con la ruta obtenida de los genes.
        '''
        ruta = "Recomended path: " + self.__str__()
        return ruta
    
    def __str__(self):
        cad = ""
        for cd in self.genes:
            cad += cd
            cad += " -> "
        cad += self.genes[0]
        return cad
    
    # Mecanismos de variación
    def cruza(self, madre):
        '''
        Se cruza a los padres para obtener nuevos individuos 
        Parameters
        ----------
        madre : Individuo
            Se cruzara con el padre.
        Returns
        -------
        obj1 : Indivduo
            Nuevo individuo.
        obj2 : Individuo
            Nuevo Individuo.
        '''
        hijo = self.genes[0:int(len(self.genes)/2)]
        hijo.extend(madre.genes[int(len(self.genes)/2):])
        hija = madre.genes[0:int(len(self.genes)/2)]
        hija.extend(self.genes[int(len(self.genes)/2):])
        obj1 = Individuo(self.ciudades)
        obj2 = Individuo(self.ciudades)
        obj1.genes = hijo
        obj2.genes = hija
        return obj1,obj2
    
    def mutar(self):
        '''
        Muta al individuo cambiando dos ciudades
        Returns
        -------
        None.
        '''
        indices = random.sample(range(len(self.genes)), 2)
        temp = self.genes[indices[0]]
        self.genes[indices[0]] = self.genes[indices[1]]
        self.genes[indices[1]] = temp
