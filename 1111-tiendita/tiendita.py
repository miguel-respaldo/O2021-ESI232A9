opcion_menu_principal = 0
opcion_menu_productos = 0

carrito = []
carrito_cantidad = []

nombre_archivo = "tiendita.csv"

def menu_principal():
    print("Menu principal")
    print("1. Mostrar productos")
    print("2. Mostrar carrito")
    print("3. Mostrar cuenta total")
    print("9. Salir")
    print("")

def menu_productos():
    print("Menu productos")
    print("1. Carnes frias")
    print("2. Frutas y verduras")
    print("3. Refrescos")
    print("4. Lacteos")
    print("5. Sabritas")
    print("9. Salir")
    print("")

def mostrar_producto(categoria):
    archivo = open(nombre_archivo, "r")
    productos = []
    numero = 1
    print("{:<5s}{:<20s}{:>7s}{:>7s}".format("No.", "Nombre", "Stock", "Precio"))
    for linea in archivo:
        lista = linea.split(",")
        if categoria.lower() == lista[3].strip().lower():
            productos.append(lista[0])
            print("{:<5d}{:<20s}{:>7d}{:>7.2f}".format(numero, lista[0], int(lista[2]), float(lista[1])))
            numero += 1
    print("-----------------------------------------")
    print("Elije el número de producto a comprar, o 0 para regresar")
    producto = eval(input("Opción: "))
    if producto != 0:
        cantidad = eval(input("¿Cuantos articulos deseas comprar?: "))
        carrito.append(productos[producto-1])
        carrito_cantidad.append(cantidad)

    archivo.close()

def mostrar_carrito():
    archivo = open(nombre_archivo, "r")
    carrito_precio = []
    total = 0
    for producto in carrito:
        # seek se va al principio del archivo
        archivo.seek(0)
        for linea in archivo:
            lista = linea.split(",")
            if producto.lower() == lista[0].strip().lower():
                carrito_precio.append(lista[1])
                break

    print("{:<5s}{:<20s}{:>7s}{:>10s}{:>10s}".format("No.", "Nombre", "Cantidad", "P. Unit.", "Precio"))
    for indice in range(len(carrito)):
        print("{:<5d}{:<20s}{:>7d}{:>10.2f}{:>10.2f}".format(indice+1, carrito[indice], int(carrito_cantidad[indice]), float(carrito_precio[indice]), int(carrito_cantidad[indice])*float(carrito_precio[indice])))
        total += int(carrito_cantidad[indice])*float(carrito_precio[indice])

    print("-----------------------------------------")
    print("{:>42s}{:>10.2f}".format("Total:", total))



while opcion_menu_principal != 9:
    menu_principal()
    opcion_menu_principal = eval(input("Opcion: "))

    if opcion_menu_principal == 1:
        opcion_menu_productos = 0
        while opcion_menu_productos != 9:
            menu_productos()
            opcion_menu_productos = eval(input("Opción: "))

            if opcion_menu_productos == 1: # Carnes frias
                mostrar_producto("carnes frias")
            elif opcion_menu_productos == 2: # Frutas y verduras
                mostrar_producto("frutas y verduras")
            elif opcion_menu_productos == 3:  # Regrescos
                mostrar_producto("refrescos")
            elif opcion_menu_productos == 4:  # Lacteos
                mostrar_producto("lacteos")
            elif opcion_menu_productos == 5:  # Sabritas
                mostrar_producto("sabritas")

    elif opcion_menu_principal == 2:
        mostrar_carrito()
    elif opcion_menu_principal == 3:
        print("mostrar cuenta total")


