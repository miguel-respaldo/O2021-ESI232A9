# Hacer un programa que pida un número al usuario
# e imprima desde 1 hasta ese número pero solo los pares

numero = eval(input("Escribe un número: "))

i = 1
while i <= numero:
    if i % 2 == 0:
        print(i)
    i += 1

