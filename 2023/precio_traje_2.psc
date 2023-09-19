Algoritmo precio_traje
	Leer precio_inicial_traje
	Si precio_inicial_traje > 2500 Entonces
		descuento <- precio_inicial_traje * 0.15
	FinSi
	precio_con_descuento <- precio_inicial_traje - descuento
	Escribir descuento
	Escribir precio_con_descuento
FinAlgoritmo
