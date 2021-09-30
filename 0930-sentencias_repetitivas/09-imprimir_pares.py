# Hacer un programa que pida un número al usuario
# e imprima desde 1 hasta ese número pero solo los pares

numero = eval(input("Escribe un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")