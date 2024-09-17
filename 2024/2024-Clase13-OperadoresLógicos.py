'''
Tabla de verdad

    and
        True  and True  = True
        True  and False = False
        False and True  = False
        False and False = False

    or
        True or True   = True
        True or False  = True
        False or True  = True
        False or False = False

    not
        not True  = False
        not False = True
'''

a = True
b = False
c = True

resultado = (a or b) and c
#           (True or False) and True
#           True and True
#           True


x = 10
y = 20
resultado = (x > 5) and (y < 30)
#           (10 > 5) and (20 < 30)
#           True and (20 < 30)
#           True and True
#           True

x = 10
y = 50
resultado = (x > 15) or (y == 50)
#           (10 > 15) or (50 == 50)
#           False or (50 == 50)
#           False or True
#           True

x = 5
resultado = not (x == 5)
#           not (5 == 5)
#           not True
#           False