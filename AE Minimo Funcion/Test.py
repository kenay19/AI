# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo que da los parametros para la ejecucion del archivo
Created on Wed Dec  1 19:04:48 2021
@author: omarl
"""
   
from AE import AE
opcion = "s"
while(opcion == "S" or opcion =="s"):
    ae = AE(int(input("Numero de Individuo: ")),int(input("Numero de Generaciones: ")))
    ae.evolve()
    opcion = input("Desea Continuar?S/N: ")