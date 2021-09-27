Algoritmo calificacion_con_grado
	Escribir "Escribe tu calificacion:"
	leer calificacion
	
	Si calificacion >= 90 Entonces
		Escribir "Grado A"
	SiNo
		Si calificacion >= 80 Entonces
			Escribir "Grado B"
		SiNo
			Si calificacion >= 70 Entonces
				Escribir "Grado C"
			SiNo
				Si calificacion >= 60 Entonces
					Escribir "Grado D"
				SiNo
					Escribir "Grado R"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
