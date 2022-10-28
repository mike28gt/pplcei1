#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:20:39 2022

@author: miguelcatalan
"""

numero = input("Ingrese la tabla de multipliación a generar: ")
numero = int(numero)

limiteInferior = input("Ingres el límite inferior de la tabla de multipliacación: ")
limiteInferior = int(limiteInferior)

limiteSuperior = input("Ingres el límite superior de la tabla de multipliacación: ")
limiteSuperior = int(limiteSuperior)


for i in range(limiteInferior, limiteSuperior):
    resultado = numero * i
    print(numero, " * ", i, " = ", resultado)
