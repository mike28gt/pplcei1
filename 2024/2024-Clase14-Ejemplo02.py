'''
Dada la producción de tres fábricas, escribe un programa para 
determinar si los costos de la fábrica A son menores que los de las 
fábricas B y C.
'''

# Entradas
costos_A = float(input("Costos de la fábrica A: "))
costos_B = float(input("Costos de la fábrica B: "))
costos_C = float(input("Costos de la fábrica C: "))

# Proceso
resultado = costos_A < costos_B and costos_A < costos_C

# Salida
print("¿El costo de A es menor que el costo de B y C?", resultado)