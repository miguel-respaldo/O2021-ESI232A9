archivo = open("demo2.txt","a")
archivo.write("Esta es una linea\n")
archivo.close()

archivo = open("demo2.txt","r")
print(archivo.read())