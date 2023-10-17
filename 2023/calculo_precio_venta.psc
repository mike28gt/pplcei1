Algoritmo calculo_precio_venta
	Leer codigo_producto
	Leer costo_materia_prima
	
	Si codigo_producto = 3 o codigo_producto = 4 Entonces
		costo_mano_obra <- costo_materia_prima * 0.75
	Sino 
		Si codigo_producto = 1 o codigo_producto = 5 Entonces
			costo_mano_obra <- costo_materia_prima * 0.8
		SiNo
			Si codigo_producto = 2 o codigo_producto = 6 Entonces
				costo_mano_obra <- costo_materia_prima * 0.85
			FinSi
		FinSi
	FinSi
		
	Si codigo_producto = 2 o codigo_producto = 5 Entonces
		gasto_fabricacion <- costo_materia_prima * 0.3
	SiNo
		Si codigo_producto = 3 o codigo_producto = 6 Entonces
			gasto_fabricacion <- costo_materia_prima * 0.35
		SiNo
			Si codigo_producto = 1 o codigo_producto = 4 Entonces
				gasto_fabricacion <- costo_materia_prima * 0.28
			FinSi
		FinSi
	FinSi
	
	costo_produccion <- costo_materia_prima + costo_mano_obra + gasto_fabricacion
	costo_venta <- costo_produccion + costo_produccion * 0.45
	
	Escribir costo_venta
	
FinAlgoritmo
