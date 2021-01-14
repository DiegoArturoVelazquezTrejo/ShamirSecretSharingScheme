# Biblioteca para trabajar con los parámetros de entrada
import sys
# Biblioteca para encriptar bajo el esquema de Shamir
from CriptoAlgoritmos import Encriptar_Shamir
# Biblioteca para desencriptar bajo el esquema Shamir
from DesencriptoAlgoritmos import Desencriptar_Shamir
# Biblioteca para manejar archivos
from Archivos import Archivo
# Biblioteca para solicitar la contraseña sin tener echo
import getpass
# Biblioteca para ilustrar
from Mensajes import Mensaje
'''
    Para encriptar:

    1. La opción c
    2. El nombre del archivo en el que serán guardadas las n evaluaciones del polonomio.
    3. El número total de evaluaciones requeridas (n > 2)
    4. El número mínimo de puntos necesarios para descifrar (1 < t <= n)
    5. El nombre del archivo con el documento claro
    6. Ya con el programa en ejecución, se debe solicitar al usuario una contraseña (sin hacer eco en la terminal).

    Para Desencriptar:

    1. La opción d.
    2. El nombre del archivo con, al menos t, de las n evaluaciones del polonomio.
    3. El nombre del archivo cifrado.

'''

# Método para imprimir de buena forma las shares
'''
@param: Diccionario con las claves (shares)
'''
def imprimir_claves(claves):

        contador = 1

        for i in claves.keys():

            print("Share["+str(contador)+"]: "+ str(i) + "\n clave segura: "+str(claves[i])+"\n")

            contador += 1
def uso():

    sys.stderr.write("\n\tUsage: %s < -c > <Archivo seguro> <#Shares N> <#Mínimo para desencriptar T> <Archivo con mensaje a encriptar>     (  T <= N  )\n" % sys.argv[0])

    sys.stderr.write("\n\tUsage: %s < -d > <Archivo con las contraseñas> <Archivo con el criptograma>\n\n" % sys.argv[0])

    sys.exit(1)

# Verificamos los parámetros
if ((len(sys.argv) != 6 and len(sys.argv) != 4) or (sys.argv[1] != '-d' and sys.argv[1] != '-c')):

    uso()

# Verificamos que los datos del encriado N y T sean números.
if(len(sys.argv) == 6 and (not sys.argv[3].isnumeric() or (not sys.argv[4].isnumeric()))):

    uso()

# Verificamos que N >= K
if(len(sys.argv) == 6 and (int(sys.argv[3]) < int(sys.argv[4]))):

    uso()

print(Mensaje.titulo())

if(len(sys.argv) == 6 and sys.argv[1] == '-c'):

    archivoFinal = sys.argv[2]

    N =  int(sys.argv[3])

    K =  int(sys.argv[4])

    mensaje = sys.argv[5]


    if(not Archivo.verifica_existencia(mensaje)):

        print(" Archivos no encontrados ")

        sys.exit(1)

    # Leemos el mensaje del archivo

    mensaje = Archivo.leer_archivo(mensaje)

    shamir = Encriptar_Shamir()

    # Pedimos la llave

    llave = getpass.getpass("Ingresa una clave segura: ")

    criptograma, shares = shamir.encriptar(mensaje, N, K, llave)

    Mensaje.mensajeEncriptado()

    print("Criptograma: "+criptograma)

    imprimir_claves(shares)

    # Guardamos en el archivo las xs y ys

    Archivo.escribir_archivo(archivoFinal, shares)

    Archivo.sobreescribir_archivo(sys.argv[5], criptograma)

if(len(sys.argv) == 4 and sys.argv[1] == '-d'):

    shamirD = Desencriptar_Shamir()

    archivoSeguro = sys.argv[2]

    criptograma = sys.argv[3]

    if(not Archivo.verifica_existencia(archivoSeguro) and not Archivo.verifica_existencia(criptograma)):

        print(" Archivos no encontrados ")

        sys.exit(1)

    criptograma = Archivo.leer_archivo(criptograma)

    xs, ys = Archivo.leer_archivo_num(archivoSeguro)

    mensaje_final = shamirD.desencriptar(criptograma, xs, ys)

    print("\n\t\t\t################## MENSAJE DESENCRIPTADO ##################\n")

    print(mensaje_final)
