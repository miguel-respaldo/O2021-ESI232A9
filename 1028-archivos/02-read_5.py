archivo = open("demo.txt", "r")

print("Las primeras 5 letras son:")
print(archivo.read(5))

print("Las siguientes 5 letras son:")
print(archivo.read(5))

print("Las siguientes 10 letras son:")
print(archivo.read(10))