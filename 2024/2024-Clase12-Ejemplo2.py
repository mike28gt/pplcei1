import math

# Entradas
x1 = input("Ingrese la coordenada en x del punto 1: ")
y1 = input("Ingrese la coordenada en y del punto 1: ")
x2 = input("Ingrese la coordenada en x del punto 2: ")
y2 = input("Ingrese la coordenada en y del punto 2: ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# Proceso
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Salidas
print("La distancia entre los dos puntos es de:", d)