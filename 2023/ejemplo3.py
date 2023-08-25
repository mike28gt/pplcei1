# Tipos de datos básicos en Python
#   Numérico
3
1000
1.23
3.14159
#   Cadenas (Texto/String)
#Miguel Catalan # esta no es una cadena válida
# Las cadenas necesitan delimitadores de inicio y fin
# Python acepta las comillas dobles y simples como delimitadores
"Miguel Catalan"
'Miguel Catalan'

"Miguel's day"
'... es "buena" persona'

# Un caracter es cualquier símbolo que se pueda generar desde el teclado
# Las cadenas con conjuntos ordenados de caracteres
"Miguel"
#123456
#012345 - Python inicia su conteo de elementos desde el 0 NO desde el 1
#       - a estos números que indican la posición de los elementos se les llama índices

# Permite determinar la cantidad de caracteres de una cadena
len("Miguel")

nombre_estudiante = "Miguel Catalan"
#                    0123456789...
#                      ...987654321  - esto para índices negativos
nombre_estudiante[2]
nombre_estudiante[5]
nombre_estudiante[-1]
nombre_estudiante[-7]

# Slicing
nombre_estudiante[0:6]
nombre_estudiante[7:14]
nombre_estudiante[-14:-8]
# Al dejar el límite inferior o superior sin ningún valor, le estamos
# indicando a Python que se utilice el primer o último elemento del conjunto
nombre_estudiante[-7:]

# Búsqueda en cadena
nombre_estudiante.find('Miguel')
nombre_estudiante.find('Catalan')
nombre_estudiante.find('Fer')

# Separar cadenas
listado_estudiantes = "Gustavo,Pedro,Roberto,Ever"
listado_estudiantes.split(",")
