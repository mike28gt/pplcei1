edad_estudiante = -1
suma_edades = 0
cantidad_estudiantes = 0

while edad_estudiante != 0:
    edad_estudiante = int(input("Ingrese la edad de un estudiante: "))
    suma_edades = suma_edades + edad_estudiante
    cantidad_estudiantes = cantidad_estudiantes + 1

edad_promedio = suma_edades / cantidad_estudiantes

print("La edad promedio de los estudiantes ingreados es de", edad_promedio)
