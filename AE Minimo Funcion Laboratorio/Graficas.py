# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Kevin Omar Lazaro Ortega
Profesor: Dr. Asdrúbal López Chau
Descripción: Permite ver la evolucion del algoritmo
Created on Thu Dec  2 14:19:56 2021
@author: omarl
"""
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
from Function import Function
class Graficas:
       
    def __init__(self,parametros):
        '''
        Crea la grafica
        Parameters
        ----------
        parametros : list
            lista para graficar la funcion.
        Returns
        -------
        None.

        '''
        a = parametros[2]
        X = np.linspace(-a,a,40)
        Y = np.linspace(-a,a,40)
        self.ff = Function()
        X,Y = np.meshgrid(X,Y)
        Z = self.ff.fitnessGraf([X,Y],parametros[4],parametros[5],parametros[6])
        fig = plt.figure()
        self.axes3d = Axes3D(fig)
        self.axes3d.plot_surface(X,Y,-Z, cmap=cm.coolwarm)
    
    def grafica(self,generacion,individuo,a,b,c):
        '''
        Grafica el punto del mejor individuo de la generacion y lo salva en un archivo png

        Parameters
        ----------
        generacion : int
            numero de generacion.
        individuo : Individuo
            individuo a graficar.
        a : int
            parametro.
        b : int
            parametro.
        c : int
            parametro.
        Returns
        -------
        None.
        '''
        x,y = individuo.getPhenotype()
        z = self.ff.fitness(individuo,a,b,c)
        self.axes3d.scatter(x,y,-z)
        plt.savefig(str(generacion)+".png")