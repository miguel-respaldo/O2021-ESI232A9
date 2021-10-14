lista = ["manzana", "pera", "limon", "kiwi", "naranja"]
nueva_lista = []

for elemento in lista:
    if "a" in elemento:
        nueva_lista.append(elemento)

print("La nueva lista es:", nueva_lista)