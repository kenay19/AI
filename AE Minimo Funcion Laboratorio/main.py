# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Permite la ejecucion del algoritmo pasandle los parametros
Created on Wed Dec  1 23:17:27 2021
@author: omarl
"""

from AE import AE
opcion = "S"
while (opcion == "S" or opcion == "s"):
    parametros = [
    int(input("Numero de Variables por Individuo: ")),
    int(input("Numero de bits por Individuo: ")),
    int(input("Intervalo de busqueda: ")),
    int(input("Tamaño de la poblacion: ")),
    int(input("Constante a: ")),
    int(input("Constante b: ")),
    int(input("Constante c: ")),
    int(input("Numero de Generaciones: "))]
    ae = AE(parametros)
    ae.evolve()
    opcion = input("Desea Continuar? S/N: ")