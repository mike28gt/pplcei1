#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:21:32 2022

@author: miguelcatalan
"""

pago_por_hora = float(input("Ingrese pago por hora: "))

dia = 1
acumulador_horas = 0
contador = 1

while (dia <= 6) :
    horas_trabajadas_dia = float(input("Ingrese horas trabajadas del día: "))
    acumulador_horas = acumulador_horas + horas_trabajadas_dia
    dia = dia + 1
    
total_a_pagar = acumulador_horas * pago_por_hora;

print("Total de horas trabajada: ", acumulador_horas)
print("El total a pagar es: ", total_a_pagar)