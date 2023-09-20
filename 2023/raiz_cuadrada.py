import math

base = float(input("Ingrese número para calcular la raíz cuadrada: "))

raiz_cadrada_1 = base ** (1/2)
print("Raiz cuadrada del número ingresado (forma 1)",raiz_cadrada_1)

raiz_cuadrada_2 = pow(base, 1/2)
print("Raiz cuadrada del número ingresado (forma 2)",raiz_cuadrada_2)

raiz_cuadrada_3 = math.sqrt(base)
print("Raiz cuadrada del número ingresado (forma 3)",raiz_cuadrada_3)