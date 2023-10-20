contador_meses = 0
total_ahorro_mes = 0
total_ahorro_anual = 0

while contador_meses < 12:
    monto_ahorrado_mes = float(input("Ingrese monto ahorrado para el mes:"))
    total_ahorro_mes = total_ahorro_mes + monto_ahorrado_mes
    print("El total ahorrado a este mes es: ", total_ahorro_mes)
    total_ahorro_anual = total_ahorro_anual + monto_ahorrado_mes
    contador_meses = contador_meses + 1

print("El total ahorrado durante el año es ", total_ahorro_anual)

