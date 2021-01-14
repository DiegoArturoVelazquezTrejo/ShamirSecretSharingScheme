import sys

from CriptoAlgoritmos import Encriptar_Shamir

from DesencriptoAlgoritmos import Desencriptar_Shamir

'''
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
        sys.exit(1)

    #NUM, MOD = int(sys.argv[1]), int(sys.argv[2])


    Para encriptar:

    1. La opción c
    2. El nombre del archivo en el que serán guardadas las n evaluaciones del polonomio.
    3. El número total de evaluaciones

'''
mensaje = "El semestre nos la pela"

llave = "mario12345hola"

N = 20

T = 14

encshamir = Encriptar_Shamir()

criptograma, xs, ys = encshamir.encriptar(mensaje, N, T, llave)

desencrip = Desencriptar_Shamir()

minimo_xs = []

minimo_ys = []

for i in range(0, 15):

    minimo_xs.append(xs[i])
    
    minimo_ys.append(ys[i])

mensajeFinal = desencrip.desencriptar(criptograma, minimo_xs, minimo_ys)

print(mensajeFinal)
