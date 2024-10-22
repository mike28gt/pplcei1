"""
Dado un correo electrónico, extraer el nombre de usuario 
(parte antes del símbolo @) y el dominio (parte después del 
símbolo @).
"""

correo_electronico = "mcatalanl1@miumg.edu.gt"
#print(correo_electronico.find("@"))
indice_arroba = correo_electronico.find("@")
usuario = correo_electronico[0:indice_arroba]
dominio = correo_electronico[indice_arroba+1:]

print(usuario)
print(dominio)

