#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:27:39 2022

@author: miguelcatalan
"""

cantidad_articulos = input("Ingrese la cantidad de artículos: ")
cantidad_articulos = int(cantidad_articulos)

acumulador_precios_con_descuento = 0

for numero_articulo in range(1, cantidad_articulos + 1):
    
    precio_articulo = input("Ingrese el precio del artículo: ")
    precio_articulo = float(precio_articulo)
    
    if (precio_articulo >= 200):
        porcentaje_descuento = 0.15
    elif (precio_articulo > 100 and precio_articulo < 200):
        porcentaje_descuento = 0.12
    else:
        porcentaje_descuento = 0.10
        
    descuento = precio_articulo * porcentaje_descuento
    precio_articulo_con_descuento = precio_articulo - descuento
    acumulador_precios_con_descuento = acumulador_precios_con_descuento + precio_articulo_con_descuento
    print("Precio: ", precio_articulo, " Descuento: ", descuento)
    
print ("Total a pagar: ", acumulador_precios_con_descuento)