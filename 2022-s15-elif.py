#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:24:56 2022

@author: miguelcatalan
"""
import math

radio = input("Ingrese el radio: ")

radio = int(radio)

if radio > 0:
    print("")
    print("1.- Calcular diámetro")
    print("2.- Calcular perímetro")
    print("3.- Calcular área") 
    resultado = input("Ingrese la opción que desea calcular: ")
    resultado = int(resultado)
    
    if resultado == 1:
        diametro = 2 * radio
        print(diametro)
    elif resultado == 2:
        perimetro = 2 * math.pi * radio
        print(perimetro)
    elif resultado == 3:
        area = math.pi * radio**2
        print(area)
    else:
        print("El resultado que desea visualizar no es válido")
                
else:
    print("El radio debe ser mayor que 0")
