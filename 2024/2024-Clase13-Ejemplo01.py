tiempo_operacion = input("Tiempo de operacion (horas): ")
produccion = input("Producción (unidades): ")

tiempo_operacion = float(tiempo_operacion)
produccion = float(produccion)

'''
Una máquina es considerada eficiente si su tiempo de operación 
es menor o igual a 8 horas y su producción es mayor a 100 unidades. 
Escriba un programa que determine si una máquina es eficiente basándose 
en su tiempo de operación y producción.
'''

es_eficiente = tiempo_operacion <= 8 and produccion > 100

print(es_eficiente)
