archivo = open("numeros.txt","r")

suma = 0
for linea in archivo:
    numero = eval(linea)
    suma += numero

print("La suma es", suma)
