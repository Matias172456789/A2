import random 

Clave = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud = int(input("Ingresa la longitud de tu contraseña"))

Elemento = ""
for i in range (Longitud):
    Elemento += random.choice(Clave)

print(Elemento)








