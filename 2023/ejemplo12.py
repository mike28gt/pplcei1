codigo_producto = int(input("Ingrese el código del producto: "))
costo_materia_prima = int(input("Ingrese el costo de la materia prima: "))

# Calcular el costo de la mano de obra
if codigo_producto == 3 or codigo_producto == 4:
    costo_mano_obra = costo_materia_prima * 0.75
elif codigo_producto == 1 or codigo_producto == 5:
    costo_mano_obra = costo_materia_prima * 0.8
elif codigo_producto == 2 or codigo_producto == 6:
    costo_mano_obra = costo_materia_prima * 0.85

# Calcular el gasto de fabricación
if codigo_producto == 2 or codigo_producto == 5:
    gasto_fabricacion = costo_materia_prima * 0.3
elif codigo_producto == 3 or codigo_producto == 6:
    gasto_fabricacion = costo_materia_prima * 0.35
elif codigo_producto == 1 or codigo_producto == 4:
    gasto_fabriacion = costo_materia_prima * 0.28

costo_produccion = costo_materia_prima + costo_mano_obra + gasto_fabricacion
costo_venta = costo_produccion + costo_produccion * 0.45

print("El costo de venta es de:", costo_venta);