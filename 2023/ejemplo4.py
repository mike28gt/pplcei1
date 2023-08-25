# Continuación del tipo de dato texto (string/cadena)

# Convertir texto a mayúsculas
texto = "Guatemala feliz que tus aras, no profane jamás el verdugo..."
texto.upper()

# Convertir texto a minúsculas
texto = "DOS Y DOS SON CUATRO, CUATRO Y DOS SON SEIS"
texto.lower()

# Evaluar si los caracteres de una cadena son letras
texto = "a"
texto.isalpha()

texto = "1"
texto.isalpha()

texto = "14avenida3-23"
texto.isalpha()

texto = "catorceavenidatresguionventitres"
texto.isalpha()

# Eliminación de espacios en blanco al inicio de una cadena
texto = "  Miguel"
texto.lstrip()

texto = "Miguel    "
texto.rstrip()

texto = "    Miguel     Catalan    "
#        123456789
texto.strip()

# Cadenas son inmutables. La inmutabilidad se refiere a que el dato no puede ser modificado
texto[8] = "r"

#
texto = "Miguel"
texto.replace("g", "r")

# Tipo de booleano
True  # 1
False # 0 
true
false 


type(365)
type(3.14159)
type("Miguel")
type(True)

