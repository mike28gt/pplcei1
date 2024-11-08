"""
numero = input("Ingrese un número real: ")
numero = float(numero)

if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo")
"""



cantidad_lapices = input("Ingrese la cantidad de lápices a comprar: ")
cantidad_lapices = int(cantidad_lapices)

if cantidad_lapices >= 1000:
    precio = 0.85
else:
    precio = 0.90

total_pagar = precio * cantidad_lapices

print("El total a pagar es de", total_pagar)