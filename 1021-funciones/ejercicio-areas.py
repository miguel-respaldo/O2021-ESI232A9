import math

def menu():
    print("------------------------")
    print("Menu")
    print("1. Calcular el área de un rectángulo.")
    print("2. Calcular el área de un triangulo.")
    print("3. Calcular el área de un cuadrado.")
    print("4. Calcular el área de un circulo.")
    print("5. Salir")
    print("")

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    #return 3.1416 * radio * radio
    #return 3.1416 * radio**2
    return math.pi * radio**2

opcion = 0

while opcion != 5:
    menu()
    opcion = eval(input("Opcion: "))

    if opcion == 1:  # Área rectangulo
        base = eval(input("¿Cual es la medida de la base?: "))
        altura = eval(input("¿Cual es la medida de la altura?: "))
        resultado = area_rectangulo(base, altura)
        print("El área del rectángulo es:", resultado)
    elif opcion == 2: # Área triangulo
        base = eval(input("¿Cual es la medida de la base?: "))
        altura = eval(input("¿Cual es la medida de la altura?: "))
        resultado = area_triangulo(base, altura)
        print("El área del triángulo es:", resultado)
    elif opcion == 3: # Area cuadrado
        lado = eval(input("¿Cual es la medida del lado?: "))
        resultado = area_rectangulo(lado, lado)
        print("El área del cuadrado es:", resultado)
    elif opcion == 4: # Area circulo
        radio = eval(input("¿Cual es la medida del radio?: "))
        resultado = area_circulo(radio)
        print("El área del circulo es:", resultado)