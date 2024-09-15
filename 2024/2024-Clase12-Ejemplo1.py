import math

# Entradas
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")

# Para convertir un dato de tipo texto a un dato de tipo númerico podemos
# utilizar las instrucciones: 
# - int() : convierte un dato de tipo texto a un dato numérico entero
# - float() : convierte un dato de tipo texto a un dato numérico real

a = float(a)
b = float(b)
c = float(c)

# Proceso

# a = 1
# b = 2
# c = 3
x1 = (-b + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)
#   -2 + ((2**2) - 4 * 1 * 3) ** (1/2) / 2 * 1
#   -2 + (4 - 4 * 1 * 3) ** (1/2) / 2 * 1
#   -2 + (4 - 4 * 3) ** (1/2) / 2 * 1
#   -2 + (4 - 12) ** (1/2) / 2 * 1
#   -2 + -8 ** (1/2) / 2 * 1
#   -2 + -8 ** 0.5 / 2 * 1
#   -2 + -8 ** 0.5 / 2 * 1
#   -2 + 2.82 imaginario / 2 * 1
#   No proporciona el resultado correcto, por lo que se deben utilizar
#   operadores de agrupación para resolver primero el numerador y después
#   el denominador.

x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Salida
print("El valor de X1 es:", x1)
print("El valor de X2 es:", x2)
