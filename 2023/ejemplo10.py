descuento = 0
precio_inicial_traje = int(input("Ingrese precio de traje: "))
if precio_inicial_traje > 2500 : 
    descuento = precio_inicial_traje * 0.15
else :
    descuento = precio_inicial_traje * 0.05
precio_con_descuento = precio_inicial_traje - descuento
print("El descuento del traje es de:",descuento)
print("El precio con descuento del traje es de:",precio_con_descuento)