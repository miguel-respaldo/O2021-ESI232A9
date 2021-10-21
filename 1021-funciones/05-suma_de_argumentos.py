def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("La suma total es:", resultado)

suma(1,2,3)
suma(5,5,5,5,5,5)
suma(3,2)
suma(2)