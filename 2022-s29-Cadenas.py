#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:31:45 2022

@author: miguelcatalan
"""

a = 3
b = 3.14159
c = True
d = '4'

"""Las cadenas son tipos de datos
estructurados, los cuales están compuestos
por un conjunto de caracteres."""
f = 'Mi mamá me mima'


"""Manipulación de cadenas """
saludo = 'Hola! mi nombre es '
nombre = 'Miguel '

union_cadenas = saludo + nombre

multiples_cadenas = nombre * 3

entero = int(d)
real = float('5.123545')

numero_entero = 3456
cadena_de_entero = str(numero_entero)

numero_real = 892.123565
cadena_de_numero_real = str(numero_real)

nombre_mayuscula = nombre.upper()

nombre_minuscula = nombre.lower()

inicial_mayuscula = nombre_mayuscula.title()

inicial_mayuscula = 'miguel alejandro'.title()

"""Caracteres de escape en cadenas"""

parrafo = "\tEsta es la primera linea \n\t\tEsto es la segunda linea"
print(parrafo)

otro_parrafo = 'Esta es una diagonal invertida: \\ '
otro_parrafo = '.. entonces exclamó: \'Oh Dios!\' '
otro_parrafo = ".. entonces exclamó: \"Oh Dios!\" "
print(otro_parrafo)


"""Longitud de cadenas"""
cadena = "Esto es una cadena"
tamanio_cadena = len(cadena)

"""Indexacion de cadenas"""
#         123456...
#         012345...
cadena = "Esto es una cadena"
print(cadena[10])
print(cadena[5])

"""Recorrido de una cadena caracter por caracter"""
for i in range(len(cadena)):
    print(cadena[i])
    
