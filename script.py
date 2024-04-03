import json
from usuario import Usuario

with open("usuarios.txt") as productos:
    #Empieza leyendo la primera linea, y por cada iteracion va avanzando por el puntero
    linea = productos.readline()
    #Minentras linea exista, seguira el loop
    while linea:
        try:
            #Intenta leer la linea actual
            usuario = json.loads(linea)

        except Exception as e:
            #Al haber un error, 
            with open("error.log", "a+") as log:
                #Escribe dentro del archivo, el mensaje
                log.write(f"[Error: {e}\n")
        finally:
            #Avanza de linea al terminar el try
            linea = productos.readline()
