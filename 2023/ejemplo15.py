# Cuando se conoce la cantidad de veces que se desea repetir el
# conjunto de instrucciones
#contador = 0
#while contador < 12:
#    numero = int(input("Ingrese un numero: "))
#    contador = contador + 1

# Cuando NO se conoce a cantidad de veces que se desea repetir el
# conjunto de instrucciones pero SI se conoce la condición de parada
#numero = -1
#while numero != 0:
#    numero = int(input("Ingrese un numero: "))


# La estructura de control repetitiva for se suele utilizar
# cuando se conoce la cantidad de veces que se desea repetir 
# un conjunto de instrucciones

# La estructura de control repetitiva for necesita conocer 
# cual es el listado de elementos que va a iterar

#lista_estudiantes = ["Gustavo", "Chelsea", "Gerardo", "Ricardo", "Edwin"]

#for nombre in ["Gustavo", "Chelsea", "Gerardo", "Ricardo", "Edwin"]:
#    print(nombre)

#for nombre in lista_estudiantes:
#    print(nombre)

#for numero in range(10, 201): # [1,2,3,4,5,....99]
#    print(numero)

total_ahorro_mes = 0
total_ahorro_anual = 0

#while contador_meses < 12:
#for mes in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
#meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#for mes in meses:
for mes in range(1,13):
    monto_ahorrado_mes = float(input("Ingrese monto ahorrado para el mes:"))
    total_ahorro_mes = total_ahorro_mes + monto_ahorrado_mes
    print("El total ahorrado a este mes es: ", total_ahorro_mes)
    total_ahorro_anual = total_ahorro_anual + monto_ahorrado_mes

print("El total ahorrado durante el año es ", total_ahorro_anual)