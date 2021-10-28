archivo = open("demo2.txt","a")
archivo.write("Woops! ya se borro\n")
archivo.close()

archivo = open("demo2.txt","r")
print(archivo.read())