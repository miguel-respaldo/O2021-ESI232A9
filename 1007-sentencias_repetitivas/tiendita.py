opcion_menu_principal = 0
opcion_menu_productos = 0

while opcion_menu_principal != 9:
    print("Menu principal")
    print("1. Mostrar productos")
    print("2. Mostrar carrito")
    print("3. Mostrar cuenta total")
    print("9. Salir")
    print("")
    opcion_menu_principal = eval(input("Opcion: "))

    if opcion_menu_principal == 1:
        opcion_menu_productos = 0
        while opcion_menu_productos != 9:
            print("Menu productos")
            print("1. Carnes frias")
            print("2. Frutas y verduras")
            print("3. Refrescos")
            print("4. Lacteos")
            print("5. Sabritas")
            print("9. Salir")
            print("")
            opcion_menu_productos = eval(input("Opción: "))
    elif opcion_menu_principal == 2:
        print("Mostrar carrito")
    elif opcion_menu_principal == 3:
        print("mostrar cuenta total")


