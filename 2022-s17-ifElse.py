#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:04:32 2022

@author: miguelcatalan
"""

import math

a = input("Ingrese valor para a: ")
b = input("Ingrese valor para b: ")
c = input("Ingrese valor para c: ")

a = int(a)
b = int(b)
c = int(c)

if a != 0:
    x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
    x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)

    print("El valor de x1 es", x1)
    print("El valor de x2 es", x2)
else:
    x = -c / b
    print("el valor de x es", x)
