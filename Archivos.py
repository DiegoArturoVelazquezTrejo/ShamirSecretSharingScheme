# Biblioteca para verificar la existencia de archivos
import os.path
'''
Clase para trabajar con archivos
'''
class Archivo:

    # Método para leer de un archivo
    '''
    @param: Nombre del archivo
    @return: Contenido del archivo
    '''
    @staticmethod
    def leer_archivo(nombre):

        f = open(nombre, "r")

        mensaje = ""

        for x in f:

            mensaje += x

        f.close()

        return mensaje
    # Método para escribir en un archivo
    '''
    @param: Nombre del archivo
    @param: Contenido que se escribirá en el archivo (es un diccionario)
    '''
    @staticmethod
    def escribir_archivo(nombre, contenido):

        if(not os.path.isfile(nombre)):

            f = open(nombre, "x")

        else:

            f = open(nombre, "w")

        print("Escribiendo en archivo ... ")

        mensaje = ""

        for i in contenido.keys():

            mensaje += str(i) + " " + str(contenido[i]) + "\n"

        f.write(mensaje)

        f.close()

    # Método para sobreescribir un archivo
    '''
    @param: Nombre del archivo
    @param: Contenido del archivo
    '''
    @staticmethod
    def sobreescribir_archivo(nombre, contenido):

        f = open(nombre, 'w')

        print("Sobrescribiendo en archivo ... ")

        f.write(contenido)

        f.close()

    # Método para leer archivos numéricos generados a partir de un diccionario
    '''
    @param: Nombre del archivo
    @return: Array xs, Array ys
    '''
    @staticmethod
    def leer_archivo_num(nombre):
        a = []

        b = []

        f = open(nombre, "r")

        for x in f:

            renglon = x.split()

            a.append(int(renglon[0]))

            b.append(int(renglon[1]))

        f.close()

        return a, b

    # Método para verificar la existencia del archivo:
    '''
    @param: Nombre del archivo
    @return: True si existe, False de lo contrario
    '''
    @staticmethod
    def verifica_existencia(nombre):

        return os.path.isfile(nombre)
