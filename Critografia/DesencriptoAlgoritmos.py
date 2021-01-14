# Biblioteca con algoritmos de hasheo
import hashlib
# Algoritmo para generar la clave segura
from hashlib import sha256
# Biblioteca con los algoritmos de criptografía: algoritmo AES
from Crypto.Cipher import AES
# Biblioteca que contiene al objeto Polinomio
from Polinomio import Polinomio
# Biblioteca con los métodos para el método de Interpolación de Lagrange
from LagrangeCero import LagrangeCero
'''
Clase que sigue el esquema Shamir Secret Sharing para desencriptar un mensaje
'''
class Desencriptar_Shamir:
    # Constructor de la clase
    def __init__(self):
        self.campo_zp_primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    '''
    Método para generar un polonomio a partir de las evaluaciones
    @param: Vector con las evaluaciones en x
    @param: Vector con las evaluaciones en y
    @return: Polinomio resultante de aplicar el método de Interpolación de Lagrange
    '''
    def generar_polinomio(x_i, y_i):

        lagrangeZp = LagrangeCero(self.campo_zp_primo)

        evaluacion0_lagrange = lagrangeZp.lagrange(x_i, y_i)

        return evaluacion0_lagrange

    '''
    Método para desencriptar basado en el esquema Shamir Secret Sharing
    @param: Mensaje a desencriptar
    @param: Evaluaciones
    '''
    def desencriptar(mensaje, x_i, y_i):
        clave_segura = self.generar_polinomio(x_i, y_i)

        # Creamos un objeto de tipo AESCipher para poder utilizar los algoritmos de cifrado

        aes = AESCipher()

        mensaje = aes.desencriptar(mensaje, clave_segura)

        return mensaje
