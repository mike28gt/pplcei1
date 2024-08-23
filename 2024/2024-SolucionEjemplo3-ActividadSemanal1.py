import math

# input(): sirve para leer/obtener datos
# print(): sirve para escribir/mostrar datos
# a = b: sirve para darle un nombre (a) a un valor (b)

R = input()
H = input()

R = int(R)
H = int(H)

altura_triangulo = math.sqrt((H*H) - (R*R))
area_triangulo = (R * altura_triangulo) / 2
area_triangulo_total = area_triangulo * 2

area_circunferencia = 3.159 * (R*R)
area_semicircunferencia = area_circunferencia / 2

area_total = area_triangulo_total + area_semicircunferencia

print(area_total)





