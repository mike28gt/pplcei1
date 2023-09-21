Algoritmo precio_traje
	Leer precio_inicial_traje
	Si precio_inicial_traje > 2500 Entonces
		descuento <- precio_inicial_traje * 0.15
	Sino
		Si precio_inicial_traje = 1500 Entonces
			descuento <- precio_inicial_traje * 0.10
		SiNo
			descuento <- precio_inicial_traje * 0.05
		FinSi
	FinSi
	precio_con_descuento <- precio_inicial_traje - descuento
	Escribir descuento
	Escribir precio_con_descuento
FinAlgoritmo
