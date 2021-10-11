lista = [] # esto es una lista vacia
# lista = list() # esta es otra lista vacia

fruta = "ejemplo"

while fruta != "":
    fruta = input("Escribe el nombre de una fruta: ")
    if fruta != "":
        lista.append(fruta)

print("La lista final es:", lista)