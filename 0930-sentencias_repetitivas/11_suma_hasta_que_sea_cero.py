# Hacer una suma de numeros hasta que el usuario
# ingrese el valor de cero y impra el resultado

print("Este programa suma números hasta que ingreses cero.")

suma = 0
numero = 1

while numero != 0:
    numero = eval(input("Ingresa un número: "))
    suma += numero
print("La suma es:", suma)