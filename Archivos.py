# Biblioteca para verificar la existencia de archivos
import os.path

# Biblioteca para trabajar con el sistema
import sys

# Biblioteca para trabajar con archivos .doc #  pip3 install python-docx
import docx

# Biblioteca para trabajar con archivos PDF # pip3 install PyPDF2
import pdfkit    # pip3 install pdfkit
import PyPDF2

'''
Clase para trabajar con archivos
'''
class Archivo:

    #Método para leer archivos con terminación .doc
    '''
    @param: Nombre del archivo
    @return: Contenido del archivo
    '''
    def leer_doc(nombre):

        try:

            doc = docx.Document(nombre)

            all_paras = doc.paragraphs

            mensaje = ""

            for para in all_paras:

                mensaje += para.text + "\n"

            return mensaje

        except:

            print("Se ha generado un error leyendo "+nombre)

            sys.exit(1)

    # Método para leer archivos con terminación .pdf
    '''
    @param: Nombre del archivo
    @return: Contenido del archivo
    '''
    def leer_pdf(nombre):

        try:

            pdfFileObj = open(nombre, 'rb')

            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            texto = ""

            for i in range(0, pdfReader.numPages):

                pageObj = pdfReader.getPage(0)

                texto += pageObj.extractText()+"\n"

            return texto

        except:

            print("Se ha generado un error leyendo "+nombre)

            sys.exit(1)

    # Método para leer de un archivo
    '''
    @param: Nombre del archivo
    @return: Contenido del archivo
    '''
    def leer_archivo_normal(nombre):

        try:

            f = open(nombre, "r")

            mensaje = ""

            for x in f:

                mensaje += x

            f.close()

            return mensaje

        except:

            print("Se ha generado un error leyendo "+nombre)

            sys.exit(1)

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

        try:

            f = open(nombre, 'w')

            print("Sobrescribiendo en archivo ... ")

            f.write(contenido)

            f.close()

        except:

            print("Se ha generado un error sobreescribiendo en "+nombre)

            sys.exit(1)

    # Método para leer archivos numéricos generados a partir de un diccionario
    '''
    @param: Nombre del archivo
    @return: Array xs, Array ys
    '''
    @staticmethod
    def leer_archivo_num(nombre):

        try:
            a = []

            b = []

            f = open(nombre, "r")

            for x in f:

                renglon = x.split()

                a.append(int(renglon[0]))

                b.append(int(renglon[1]))

            f.close()

            return a, b

        except:

            print("Se ha generado un error leyendo el archivo seguro. ")

            sys.exit(1)

    # Método para verificar la existencia del archivo:
    '''
    @param: Nombre del archivo
    @return: True si existe, False de lo contrario
    '''
    @staticmethod
    def verifica_existencia(nombre):

        return os.path.isfile(nombre)

    # Método para leer de un archivo
    '''
    @param: Nombre del archivo
    @return: Contenido del archivo
    '''
    @staticmethod
    def leer_archivo(nombre):

        # Vamos a ver el tipo de extensión del archivo

        terminacion = nombre.split(".")[1].lower()

        if(terminacion == "docx" or terminacion == "doc"):

            return Archivo.leer_doc(nombre)

        elif(terminacion == "pdf"):

            return Archivo.leer_pdf(nombre)

        else:

            try:

                f = open(nombre, "r")

                mensaje = ""

                for x in f:

                    mensaje += x

                f.close()

                return mensaje

            except:

                print("Se ha generado un error leyendo "+nombre)

                sys.exit(1)

    # Método para generar un archivo dada la extensión
    '''
    @param: Mensaje que se guardará en el archivo
    @param: Nombre del archivo con extensión
    @param: Extensión del archivo
    '''
    @staticmethod
    def generarArchivo(contenido, nombre_archivo, extension):

        extension = extension.lower()

        # Tenemos que ver qué tipo de extensión es y con base en eso generamos el archivo

        if(extension == "txt"):

            f = open(nombre_archivo+"."+extension, "a")

            f.write(contenido)

            f.close()


    # Método para identificar la extensión de un archivo
    '''
    @param: Nombre del archivo
    '''
    @staticmethod
    def extension_archivo(nombre_archivo):
        #Buscar (".") si no esta entonces extension=".txt"(por default)
        busqueda=nombre_archivo.find(".")

        if busqueda == -1 :

            return ".txt"

        else :

            try:

                partes_nombre_archivo=nombre_archivo.split('.')

                extension=partes_nombre_archivo[-1]

                return extension

            except:

                print("Error en busqueda de extensión del archivo. ")

                sys.exit(1)
