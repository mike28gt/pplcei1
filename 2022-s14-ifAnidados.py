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
    resultado = input("Ingrese resultado que desea visualizar: ")
    
    if resultado == "diametro":
        diametro = 2 * radio
        print(diametro)
    else:
        
        if resultado == "perimetro":
            perimetro = 2 * math.pi * radio
            print(perimetro)
        else:
            if resultado == "area":
                area = math.pi * radio**2
                print(area)
            else:
                print("El resultado que desea visualizar no es válido")
                
else:
    print("El radio debe ser mayor que 0")
