# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Pruebas preliminares
Created on Fri Dec  3 22:01:51 2021
@author: omarl
"""

from FitnessFunction import FitnessFunction
from AlgoritmoEvolutivo import AlgoritmoEvolutivo
opcion = "s"
while (opcion == "S" or opcion == "s"):
    ff = FitnessFunction(input("Da una palabra: "))
    ae = AlgoritmoEvolutivo(ff, 100, 600)# Al construir un objeto AE 
                    # se le pasa la función de aptitud a usar.
    ae.evolve(500)
    opcion = input("Deseas Continuar? S/N: ")