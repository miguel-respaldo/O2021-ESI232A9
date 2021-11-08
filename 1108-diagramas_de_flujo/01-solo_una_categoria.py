archivo = open("tiendita.csv","r")

categoria = input("Escribe la categoria que quieres ver: ")

for linea in archivo:
    lista = linea.split(",")
    if categoria.lower() == lista[3].strip().lower():
        print("{:<20s} {:>6.2f}  {:>5d}".format(lista[0],float(lista[1]),int(lista[2])))

archivo.close()
