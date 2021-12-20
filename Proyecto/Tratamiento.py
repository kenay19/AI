# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Proyecto
Alumnos: Ernesto Martinez Islas, Fernando Emanuel Santacruz Lara y Kevin Omar Lazaro Ortega 
Profesor: Dr. Asdrúbal López Chau
Descripcion: Se dara un tratamiento a los datos para que pueda utilizarse correctamente
Created on Fri Nov 19 13:44:11 2021
@author: omarl
"""
import pandas as pd
class Tratamiento:
        
        def __init__(self,conn):
            '''
            Nos lee los datos de la base de datos o de un archivo csv
            Parameters
            ----------
            conn : Conexion a mysql                
            Returns
            -------
            None.

            '''
            #self.data = pd.read_sql("SELECT cantidadC,nomPro,costo,cantidadT,tipoCantidad FROM Carrito,Productos WHERE Carrito.activo=FALSE AND Productos.idProducto=Carrito.idProducto",conn)
            #a = pd.read_sql("select sum(total) as t from detalleCompra",conn)
            #self.totalCosto = a["t"][0]
            self.data = pd.read_csv("datos1.csv")
            
        def tratamientoDatos(self):
            '''
            De los datos leidos les hace un tratamiento para que solo quede con la cantidad y ventas por producto
            ademas que los etiqueta
            Returns
            -------
            dataAux : DataFrame
                Regresa un dataFrame con los datos necesarios para el algoritmo

            '''
            lenx,leny = self.data.shape
            dataAux = pd.DataFrame()
            costo = []
            cantidad = []
            cant = 0
            cost = 0
            totalCantidad = 0
            totalCosto = 0 
            etiquetas = []
            productos = list(set(self.data['nomPro']))
            for producto in productos:
                for i in range(lenx):
                    if  self.data['nomPro'][i] == producto:
                        if self.data['tipoCantidad'][i] == 1:
                            cant += self.data['cantidadC'][i]/1000
                            cost += (self.data['costo'][i]*1000)/self.data['cantidadT'][i] *self.data['cantidadC'][i]/1000
                        else:
                            cant += self.data['cantidadC'][i]
                            cost += self.data['costo'][i] * self.data['cantidadC'][i]
                totalCantidad += cant
                totalCosto += cost
                costo.append(cost)
                cantidad.append(cant)
                cost = 0
                cant = 0
            dataAux['Producto'] = productos
            dataAux['Cantidad'] = cantidad/totalCantidad
            dataAux['Venta'] = costo/totalCosto
            lenx,leny = dataAux.shape
            for i in range(lenx):
                if(dataAux["Cantidad"][i]<=0.0015 and dataAux["Venta"][i]<=0.002):
                    etiquetas.append("No Exitoso")
                elif(dataAux["Cantidad"][i]<=0.0075 and dataAux["Venta"][i]<=0.0125):
                    etiquetas.append("Comun")
                else:
                    etiquetas.append("Exitoso")
            dataAux['Etiquetas'] = etiquetas
            return dataAux
                
        def writeDocummet(self,frame,archivo):
            '''
            Escribe un documento CSV

            Parameters
            ----------
            frame : DataFrame
                Datos a escribir
            archivo : String
                Nombre del archivo

            Returns
            -------
            None.

            '''
            frame.to_csv(archivo)