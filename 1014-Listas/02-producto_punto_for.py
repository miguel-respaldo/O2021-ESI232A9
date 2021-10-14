v1 = [1, 2, 3]
v2 = [2, 2, 2]

# producto_punto = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

producto_punto = 0

#indice=0
#while indice < 3:
#    producto_punto += v1[indice]*v2[indice]
#    indice += 1

for indice in range(3):
    producto_punto += v1[indice]*v2[indice]


print("El producto punto es:", producto_punto)