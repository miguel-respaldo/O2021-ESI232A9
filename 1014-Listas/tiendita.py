opcion_menu_principal = 0
opcion_menu_productos = 0

carnes_frias = ["salchicha", "jamon", "salami", "peperoni"]
carnes_frias_precio = [30, 20, 25.5, 35.5]
carnes_frias_stock = [20, 25, 30, 35]

# Frutas y Verduras
fyv = ["manzana", "naranaja", "pera", "lechuga", "jitomate", "pepino"]
fyv_precio = [30, 30, 20.5, 10, 20, 15]
fyv_stock = [50, 50, 45, 40, 32, 35]

refrescos = ["coca", "sprite", "fanta"]
refrescos_precio = [30, 32, 35]
refrescos_stock = [20, 30, 35]

lacteos = ["leche", "queso", "crema"]
lacteos_precio = [20, 15, 17]
lacteos_stock = [50, 40, 35]

sabritas = ["papas", "doritos", "chetos"]
sabritas_precio = [10, 20, 15]
sabritas_stock = [60, 50, 55]

carrito = []
carrito_cantidad = []

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

            if opcion_menu_productos == 1: # Carnes frias
                print("No.    Nombre    Stock    Precio")
                num_elementos = len(carnes_frias)
                for i in range(num_elementos):
                    print(i,"  ",carnes_frias[i], "  ",carnes_frias_stock[i], "  ", carnes_frias_precio[i])
                print("-----------------------------------------")
                print("Elije el número de producto a comprar, o 0 para regresar")
                producto = eval(input("Opción: "))
                if producto != 0:
                    cantidad = eval(input("¿Cuantos articulos deseas comprar?: "))
                    carrito.append(carnes_frias[producto])
                    carrito_cantidad.append(cantidad)
            elif opcion_menu_productos == 2: # Frutas y verduras
                pass
            elif opcion_menu_productos == 3:  # Regrescos
                pass
            elif opcion_menu_productos == 4:  # Lacteos
                pass
            elif opcion_menu_productos == 5:  # Sabritas
                pass
    elif opcion_menu_principal == 2:
        print("Mostrar carrito")
    elif opcion_menu_principal == 3:
        print("mostrar cuenta total")


