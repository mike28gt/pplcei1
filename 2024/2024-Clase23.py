"""
a = 0
a = a + 10
print(a)
a = a + 10
print(a)
a = a + 10
print(a)

# acumulador
acumulador = 0
acumulador = acumulador + 10
print(acumulador)
acumulador = acumulador + 5
print(acumulador)
acumulador = acumulador + 100
print(acumulador)
acumulador = acumulador + 25
print(acumulador)
"""

"""
inicio 
mientras numero >= 0
    acumulador = acumulador + numero
    leer numero
escribir acumulador
fin 
"""

numero = 0
acumulador = 0

while numero >= 0:
    acumulador = acumulador + numero
    numero = int(input("Ingrese un número entero: "))

print("La sumatoria de los números positivos es:", acumulador)