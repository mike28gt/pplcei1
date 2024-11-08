#inicio 
descuento = 0
precio_traje_descuento = 0
#leer precio del traje
precio_traje = float(input("Ingrese el precio del traje: "))
#si precio del traje > 2500.00 entonces
if precio_traje > 2500 :
    #descuento = precio del traje * 0.15
    descuento = precio_traje * 0.15
#precio del traje con descuento = precio del traje - descuento
precio_traje_descuento = precio_traje - descuento
#escribir descuento
print("El descuento es de:", descuento)
#escribir precio del traje con descuento
print("El precio del traje con descuento es de:", precio_traje_descuento)
#fin 
