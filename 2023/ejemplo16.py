
def menu() :
    print("Listado de opciones")
    print("   1. Suma")
    print("   2. Resta")
    print("   3. Multiplicación")
    print("   4. División")
    opcion_elegida = int(input("Ingrese el número de la operación que desea realizar:"))


def calcular_suma() :
    primer_numero = input("Escribir primer número: ")
    segundo_numero = input("Escribir segundo número: ")
    suma = primer_numero + segundo_numero
    print("El resultado de la suma es: ", suma)

def calcular_resta() :
    primer_numero = input("Escribir primer número: ")
    segundo_numero = input("Escribir segundo número: ")
    resta = primer_numero - segundo_numero
    print("El resultado de la resta es: ", resta)

def calcular_multiplicacion() :
    primer_numero = input("Escribir primer número: ")
    segundo_numero = input("Escribir segundo número: ")
    multliplicacion = primer_numero * segundo_numero
    print("El resultado de la multiplicación es: ", multliplicacion)


def calcular_division() :
    primer_numero = input("Escribir primer número: ")
    segundo_numero = input("Escribir segundo número: ")
    division = primer_numero / segundo_numero
    print("El resultado de la division es: ", division)