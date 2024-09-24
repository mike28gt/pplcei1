'''
Una producción es considerada de calidad aceptable si el porcentaje de 
defectos es menor o igual a 5% y el total de unidades producidas es mayor 
a 1,000. Escribe un programa para verificar si una producción es de calidad 
aceptable dado el porcentaje de defectos y la cantidad de unidades 
producidas.
'''

# Entradas
porcentaje_defectos = float(input("Ingrese porcentaje de defectos de la producción: "))
unidades_producidas = float(input("Ingrese las unidades producidas: "))

# Proceso
resultado = porcentaje_defectos <= 0.05 and unidades_producidas > 1000

# Salida
print("La producción es de calidad:", resultado)