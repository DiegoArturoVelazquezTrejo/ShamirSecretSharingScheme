# Biblioteca con algoritmos de hasheo
import hashlib
# Algoritmo para generar la clave segura
from hashlib import sha256
# Biblioteca con los algoritmos de criptografía: algoritmo AES
from AESCipher import AESCipher
# Biblioteca que contiene al objeto Polinomio
from Polinomio import Polinomio
# Biblioteca para generar números aleatorios
import random
# Biblioteca para trabajar con el campo Zp con p primo
from CampoZP import Zp
'''
Clase que sigue el esquema Shamir Secret Sharing para encriptar un mensaje
'''
class Encriptar_Shamir:

    # Constructor de la clase
    def __init__(self):

        # Número primo que definirá nuestro campo Zp

        self.campo_zp_primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

        # Creamos una instancia de un campo Zp para operar el polinomio

        self.zp = Zp(self.campo_zp_primo)

    '''
    Método para generar un polonomio aleatoriamente en un campo Zp
    @param: Término independiente del polinomio
    @param: Grado del polinomio
    @return: Polinomio generado
    '''
    def generar_polinomio_zp(self,termino_indep, grado):

        coeficientes = []

        # Agregamos una clave de sha256 como simulacro

        coeficientes.append(termino_indep)

        for i in range(0, grado):

            coeficientes.append(self.zp.random_zp(grado))

        # Definimos el polinomio

        pol = Polinomio(grado, True, coeficientes)

        # Regresamos el polinomio

        return pol
    '''
    Método para encriptar basado en el esquema Shamir Secret Sharing
    @param: Mensaje a encriptar
    @param: Número de personas en total
    @param: Número mínimo de personas para desencriptar
    @param: Llave del usuario
    @return: El criptograma y las respectivas shares
    '''
    def encriptar(self,mensaje, N, K, llave):

        # Creamos un objeto de tipo AESCipher para poder utilizar los algoritmos de cifrado

        aes = AESCipher()
        # Generamos la contraseña clave_segura

        clave_segura = aes.sha256_numerico(llave)

        # Generamos el polinomio

        polinomio = self.generar_polinomio_zp(clave_segura, K)

        # Evaluamos en los N puntos

        diccionario_evaluaciones = {}

        xs = []

        ys = []

        for i in range(0, N):

            x = self.zp.random_zp(self.campo_zp_primo)

            while(x in diccionario_evaluaciones):

                x = self.zp.random_zp(self.campo_zp_primo)

            y = polinomio.eval(x)

            diccionario_evaluaciones[x] = y

            ys.append(y)

            xs.append(x)

        # Encriptamos el menaje

        criptograma = aes.encriptar(mensaje, str(clave_segura))

        # Regresamos el criptograma y los puntos (evaluacioness)

        return (criptograma, diccionario_evaluaciones)
