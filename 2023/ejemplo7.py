# Operadores aritméticos
#   Módulo o residuo
#           %
#   División entera
#           //
7 % 2
7 // 2

# Expresiones relacionales
#   >
8 > 2
#   >=
#   <
#   <=
#   == igual que
4 == 8      # False
10 == 10    # True
#   != diferente que
4 != 8      # True
10 != 10    # False
# El resultado de los operadores relaciones es un dato de tipo booleano.

2 + 3 > 10 - 5 
# 5 > 5
# False

# 2 + 3 = 10 - 5
2 + 3 == 10 - 5
5 == 5
True

# Expresiones lógicas
#   En estas expresiones sus operandos deben ser datos de tipo booleano
# and (y/disyunción)
True  and True      # True
True  and False     # False
False and True      # False
False and False     # False

# or (o/conjunción)
True  or True       # True
True  or False      # True
False or True       # True
False or False      # False

# not (negación/complemento)
#   Operador unario
not True    # False
not False   # True

2 + 1 < 7 - 5 and 25 < 30
# 3 < 2 and 25 < 30
# False and True
# False

# Lectura de datos en la línea de comandos de Python
# input()

dato = input()

# Mostrar datos en la línea de comandos
print(dato)