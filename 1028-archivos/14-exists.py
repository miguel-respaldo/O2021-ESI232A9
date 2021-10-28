import os

if os.path.exists("carpeta1"):
    os.rmdir("carpeta1")
    print("Ya borre la carpeta/directorio llamada carpeta1")
else:
    print("La caperta/directorio no existe.")