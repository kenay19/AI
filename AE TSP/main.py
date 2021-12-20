# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Archivo en el cual ejecutaremos todo el codigo
Created on Wed Sep 15 19:13:51 2021
@author: omarl
"""

from AlgoritmoEvolutivo import AlgoritmoEvolutivo
import numpy as np

def menu():
    print("1) distancias")
    print("2) distancias1")
    print("3) distancias2")
    print("4) distancias3")
    print("5) distancias4")
    print("6) distancias5")
    op = input("Escoga un archivo: ")
    if op == "1":
        return "distancias.csv"
    elif op == "2":
        return "distancias1.csv"
    elif op == "3":
        return "distancias2.csv"
    elif op == "4":
        return "distancias3.csv"
    elif op == "5":
        return "distancias4.csv"
    elif op == "6":
        return "distancias5.csv"
    else:
        print("Opcion invalida escoge una nueva ")
        return menu()

def listas(aux):
    temp = []
    real = []
    ciudades = []
    for i in range(len(aux)):
        temp.append(aux[i].split(","))
        real.append([])
        ciudades.append("C"+str(i+1))
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            real[i].append(float(temp[i][j]))
    return ciudades,real
op = "S"
while op == "S" or op == "s":
    ciudades,distancias = listas(np.loadtxt(menu(),dtype=str,delimiter="\n"))
    ae = AlgoritmoEvolutivo(ciudades,distancias,int(input("Da el numero de individuos por generacion: ")))
    ae.evolve(int(input("Da el numero de generaciones: ")))
    op = input("¿Desea Continuar? S/N: ")

    