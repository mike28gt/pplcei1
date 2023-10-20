Algoritmo calculo_ahorros
	Mientras contador_meses < 12
		Leer monto_ahorrado_mes
		total_ahorro_mensual <- total_ahorro_mensual + monto_ahorrado_mes
		Escribir total_ahorro_mensual
		
		total_ahorro_anual <- total_ahorro_anual + monto_ahorrado_mes
		contador_meses <- contador_meses + 1
	FinMientras
	Escribir total_ahorro_anual
FinAlgoritmo
