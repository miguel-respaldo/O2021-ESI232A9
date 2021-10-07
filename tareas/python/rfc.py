nombre = input("Escribe tu nombre: ")
apellido_paterno = input("Escribe tu apellido paterno: ")
apellido_materno = input("Escribe tu apellido materno: ")
dia = input("Ingresa tu dia de nacimiento: ")
mes = eval(input("Ingresa tu mes de nacimiento: "))
anio = eval(input("Ingresa tu año de nacimiento: "))

RFC = apellido_paterno[:2].upper() + apellido_materno[0].upper() + nombre[0].upper()

if anio > 1000:
    RFC = RFC + str(anio)[2:]
else:
    RFC = RFC + str(anio)

if mes >= 10:
    RFC = RFC + str(mes)
else:
    RFC = RFC + "0" + str(mes)

if len(dia) == 2:
    RFC = RFC + dia
else:
    RFC = RFC + "0" + dia

print("El RFC es:", RFC)