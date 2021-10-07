import random

numero_computadora = random.randint(1,10)

numero_usuario = eval(input("Avidina que número estoy pensando: "))

while numero_usuario != numero_computadora:
    print("No, ese no es")
    numero_usuario = eval(input("Intenta con otro número: "))

print("Felicidades Adivinaste!")