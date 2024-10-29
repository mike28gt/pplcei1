"""
Construir una cadena formada por el saludo “Hola” repetido 3 veces, 
seguido de una coma y el nombre de una persona.
"""

"""
nombre = input("Ingrese un nombre: ")
saludo = "Hola " * 3
mensaje = saludo + ", " + nombre
print(mensaje)
"""


"""
Dada una cadena que representa un mensaje, encontrar la primera aparición 
de la palabra "python" y reemplazarla por "Python" con mayúscula inicial.
"""

"""
mensaje = input("Escriba un mensaje a continuación: ")
indice = mensaje.find("python")
nuevo_mensaje = mensaje.replace("python", "Python", 1)
print("La primer aparición de la palabra python está en el índice:", indice)
print(nuevo_mensaje)
"""

"""
Dado un párrafo, dividirlo en palabras y luego unirlas en una cadena 
usando guiones (-) entre cada palabra.
"""

"""
parrafo = input("Ingrese un parrafo: ")
palabras = parrafo.split()
nueva_cadena = "-".join(palabras)
print(nueva_cadena)
"""

"""
Dado un nombre con espacios adicionales al principio y al final, eliminar 
los espacios extra que se encuentran al inicio y al final del nombre. 
Muestre el nombre del archivo sin espacios extras, sin espacios extras 
solamente a la derecha y sin espacios extras solamente a la izquierda.
"""

"""
nombre = input("Ingrese un nombre: ")
nombre_sin_espacios = nombre.strip()
nombre_sin_espacios_a_la_derecha = nombre.rstrip()
nombre_sin_espacios_a_la_izquierda = nombre.lstrip()

print("El nombre sin espacios en blanco es:", nombre_sin_espacios)
print("El nombre sin espacios en blanco a la derecha es:", nombre_sin_espacios_a_la_derecha)
print("El nombre sin espacios en blanco a la izquierda es:", nombre_sin_espacios_a_la_izquierda)
"""


"""
Dada una fecha en formato dd-mm-yyyy extraer el día, mes y año por separado.
"""            
fecha = input("Ingrese una fecha en formato dd-mm-yyyy: ")
componentes = fecha.split("-")
#    0     1       2
# ['21', '10', '2024']
print("El día es:", componentes[0])
print("El mes es:", componentes[1])
print("El año es:", componentes[2])