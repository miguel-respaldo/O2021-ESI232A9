import operaciones
import menu

opcion_menu = 0

while opcion_menu != 5:
    menu.principal()
    opcion_menu = eval(input("Opcion: "))

    if opcion_menu != 5:
        n1 = eval(input("Escribe un número: "))
        n2 = eval(input("Escribe otro número: "))

    if opcion_menu == 1:
        resultado = operaciones.suma(n1, n2)
    elif opcion_menu == 2:
        resultado = operaciones.resta(n1, n2)
    elif opcion_menu == 3:
        resultado = operaciones.multiplicacion(n1, n2)
    elif opcion_menu == 4:
        resultado = operaciones.division(n1, n2)

    if opcion_menu != 5:
        print("El resultado es", resultado)
