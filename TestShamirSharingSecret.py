# Biblioteca para encriptar bajo el esquema de Shamir
from CriptoAlgoritmos import Encriptar_Shamir

# Biblioteca para desencriptar bajo el esquema de Shamir
from DesencriptoAlgoritmos import Desencriptar_Shamir

# Biblioteca para trabajar con Archivos
from Archivos import Archivo

# Biblioteca para trabajar números aleatorios
import random

# Biblioteca para trabajar con el sistema
import sys

# Biblioteca para trabajar con el SO
import os

'''
Pruebas unitarias para el esquema de encriptado Shamir
'''

# Vamos a definir una contraseña

clave_usuario = "dfghjdbfubbfwrby6736bbsi"

# Necesitamos el documento de menensaje.txt para realizar esta prueba

mensaje = "./Test/mensaje.txt"

mensajeT = Archivo.leer_archivo(mensaje)

for i in range(0, 100):

    # Generamos aleatoriamente un K y un N

    N = random.randint(3, 40)

    K = random.randint(3, N)

    # Encriptamos

    shamir = Encriptar_Shamir()

    criptograma, shares = shamir.encriptar(mensajeT, N, K, clave_usuario)

    Archivo.escribir_archivo("claves.txt", shares)

    Archivo.sobreescribir_archivo(mensaje, criptograma)

    # Abrimos el documento con las contraseñas

    criptograma = Archivo.leer_archivo(mensaje)

    xs, ys = Archivo.leer_archivo_num("claves.txt")

    xs_aleatorias = []

    ys_aleatorias = []

    # Vamos a seleccionar aleatoriamente una cierta cantidad de veces J contraseñas entre K y N y tiene que funcionar
    for i in range(0, K):

        xs_aleatorias.append(xs[i])

        ys_aleatorias.append(ys[i])

    shamirD = Desencriptar_Shamir()

    try:

        mensaje_final = shamirD.desencriptar(criptograma, xs_aleatorias, ys_aleatorias) # Tendría que pasar estas pruebas

        print("Test desencriptado utilizando K contraseñas   ....  100%")

    except:

        print("Se pidieron como mínimo: "+str(K)+" claves para desencriptar y se están utilizando: "+str(len(xs_aleatorias))+" claves.")

        print("Error desencriptando con K contraseñas ... ")

        print("HA SUCEDIDO UN ERROR")

        sys.exit(1)

    # Seleccionaremos las N contraseñas

    xs_aleatorias = []

    ys_aleatorias = []

    for i in range(0, N):

        xs_aleatorias.append(xs[i])

        ys_aleatorias.append(ys[i])

    shamirD = Desencriptar_Shamir()

    try:

        mensaje_final = shamirD.desencriptar(criptograma, xs_aleatorias, ys_aleatorias) # Tendría que pasar estas pruebas

        mensaje_inicial = mensaje_final

        print("Test desencriptado utilizando N contraseñas   ....  100%")

    except:

        print("Se pidieron como mínimo: "+str(K)+" claves para desencriptar y se están utilizando: "+str(len(xs_aleatorias))+" claves.")

        print("Error desencriptando con K contraseñas ... ")

        print("HA SUCEDIDO UN ERROR CON EL DESENCRIPTADO!")

        sys.exit(1)


    # Seleccionamos J < K contraseñas y tenemos que esperar un error

    xs_aleatorias = []

    ys_aleatorias = []

    for i in range(0, K-1):

        xs_aleatorias.append(xs[i])

        ys_aleatorias.append(ys[i])


    try:

        mensaje_final = shamirD.desencriptar(criptograma, xs_aleatorias, ys_aleatorias)

        Archivo.sobreescribir_archivo(mensaje, mensaje_final)

        print("Error desencriptando con K - 1 claves")

        print("HA SUCEDIDO UN ERROR")

        sys.exit(1)

    except:

        print("Test desencriptando con menos de K contraseñas ...  100% ")

        Archivo.sobreescribir_archivo(mensaje, mensaje_inicial.decode("utf-8"))

os.remove("claves.txt")
