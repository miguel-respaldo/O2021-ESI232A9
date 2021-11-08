Funcion regresa <- funcion_de_python(nombre_funcion)
	regresa <- 1
	Escribir 'Ejecuta la funcion ',nombre_funcion
FinFuncion

Funcion menu ()
	Escribir ' -- Menu --'
	Escribir '1. Lista el directorio'
	Escribir '2. Agregar al directorio'
	Escribir '3. Eliminar del directorio'
	Escribir '4. Modificar del directorio'
	Escribir '5. Mostarar favoritos'
	Escribir '6. Salir'
	Escribir ''
FinFuncion

Funcion mostrar_directorio (archivo)
	Para linea<-1 Hasta archivo Hacer
		lista <- funcion_de_python('split')
		Escribir 'Nombre, Telefono, Direccion'
	FinPara
FinFuncion

Funcion agregar_al_directorio (archivo)
	Escribir 'Escribe el nombre'
	Leer nombre
	Escribir 'Escribe el telefono'
	Leer telefono
	Escribir 'Escribe la direccion'
	Leer direccion
	Escribir 'Es favorito S/N'
	Leer favorito
	fav <- ''
	Si favorito='s' Entonces
		fav <- '*'
	FinSi
	archivo <- funcion_de_python('write')
FinFuncion

Algoritmo directorio
	opcion_menu <- 1
	nombre_archivo <- 'directorio.csv'
	Si funcion_de_python('os.path.exists') Entonces
		archivo <- funcion_de_python('open')
		archivo <- funcion_de_python('archivo.write')
		archivo <- funcion_de_python('archivo.close')
	FinSi
	Mientras opcion_menu<>6 Hacer
		menu()
		Escribir 'Opcion:'
		Leer opcion_menu
		Segun opcion_menu  Hacer
			1:
				archivo <- funcion_de_python('open')
				mostrar_directorio(archivo)
				archivo <- funcion_de_python('close')
			2:
				archivo <- funcion_de_python('open')
				agregar_al_directorio(archivo)
				archivo <- funcion_de_python('close')
			3:
				Escribir ''
			De Otro Modo:
				Escribir ''
		FinSegun
	FinMientras
FinAlgoritmo
