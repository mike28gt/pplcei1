s = "esto es una cadena una"
print(s.find("a"))

print(s.replace("esto", "Esto"))
print(s.replace("una", "UNA"))

print(s.split(' '))
# ['esto', 'es', 'una', 'cadena', 'una']
print(s.split('a'))
# s = "esto es una cadena una"
# ['esto es un', ' c', 'den', ' un', '']

lista_cadenas = ['esto', 'es', 'una', 'cadena', 'una']
print(" ".join(lista_cadenas))
print(",".join(lista_cadenas))
print("-".join(lista_cadenas))

texto_en_mayusculas = s.upper()
print(s.upper())

print(texto_en_mayusculas.lower())

s = "cadena "
print(s.isalpha())

s = "cadena"
print(s.isalpha())

s = "cadenañ"
print(s.isalpha())

s = "1234"
print(s.isnumeric())

s = "12a34"
print(s.isnumeric())

s = "CAdeNA"
print(s.isalpha())


s = "  esto es una cadena  "
print(s.lstrip())

print(s.rstrip())

print(s.strip())