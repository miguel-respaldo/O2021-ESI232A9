import random

longitud = eval(input("Longitud de la cadena: "))

cadena = ""

for x in range(longitud):
    letra_num = random.randint(ord("A"), ord("Z"))
    cadena = cadena + chr(letra_num)

print("La cadena es:", cadena)

