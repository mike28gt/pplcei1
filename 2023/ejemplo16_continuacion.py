
def menu() :
    print("Listado de opciones")
    print("   1. Suma")
    print("   2. Resta")
    print("   3. Multiplicación")
    print("   4. División")
    opcion_elegida = int(input("Ingrese el número de la operación que desea realizar: "))
    
    primer_numero = float(input("Escribir primer número: "))
    segundo_numero = float(input("Escribir segundo número: "))
    
    resultado = 0.0
    if opcion_elegida == 1:
        resultado = calcular_suma(primer_numero, segundo_numero)
    elif opcion_elegida == 2:
        resultado = calcular_resta(primer_numero, segundo_numero)
    elif opcion_elegida == 3:
        resultado = calcular_multiplicacion(primer_numero, segundo_numero)
    elif opcion_elegida == 4:
        resultado = calcular_division(primer_numero, segundo_numero)

    print("El resultado de la operación es:", resultado)


def calcular_suma(primer_numero, segundo_numero) :
    # primer_numero = float(input("Escribir primer número: "))
    # segundo_numero = float(input("Escribir segundo número: "))
    suma = primer_numero + segundo_numero

    return suma
    #print("El resultado de la suma es:", suma)

def calcular_resta(primer_numero, segundo_numero) :
    # primer_numero = float(input("Escribir primer número: "))
    # segundo_numero = float(input("Escribir segundo número: "))
    resta = primer_numero - segundo_numero
    return resta
    # print("El resultado de la resta es: ", resta)

def calcular_multiplicacion(primer_numero, segundo_numero) :
    # primer_numero = float(input("Escribir primer número: "))
    # segundo_numero = float(input("Escribir segundo número: "))
    multliplicacion = primer_numero * segundo_numero
    return multliplicacion
    # print("El resultado de la multiplicación es: ", multliplicacion)


def calcular_division(primer_numero, segundo_numero) :
    # primer_numero = float(input("Escribir primer número: "))
    # segundo_numero = float(input("Escribir segundo número: "))
    division = primer_numero / segundo_numero
    return division
    #print("El resultado de la division es: ", division)

menu()