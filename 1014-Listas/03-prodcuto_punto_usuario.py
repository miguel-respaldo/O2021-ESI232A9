
dimension = eval(input("Escribe la dimensión de los vectores: "))

v1 = []
v2 = []
producto_punto = 0

for indice in range(dimension):
    numero = eval(input("Escribe un número para v1: "))
    v1.append(numero)


for indice in range(dimension):
    numero = eval(input("Escribe un número para v2: "))
    v2.append(numero)


for indice in range(dimension):
    producto_punto += v1[indice]*v2[indice]

print("El producto punto de",v1,"con",v2,"es:", producto_punto)