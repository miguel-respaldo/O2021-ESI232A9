numero = eval(input("Escribe un numero: "))

if numero > 10:
    print("Es mayor a 10")
    if numero > 20:
        print("y es mayor a 20")
    else:
        print("pero es menor a 20")
else:
    print("Es menor a 10")
