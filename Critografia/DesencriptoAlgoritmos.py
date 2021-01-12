# Biblioteca con algoritmos de hasheo
import hashlib
# Algoritmo para generar la clave segura
from hashlib import sha256
# Biblioteca con los algoritmos de criptografía: algoritmo AES
from Crypto.Cipher import AES
# Biblioteca que contiene al objeto Polinomio
from Polinomio import Polinomio
# Biblioteca con los métodos para el método de Interpolación de Lagrange
from Lagrange import Lagrange
'''
Clase que sigue el esquema Shamir Secret Sharing para desencriptar un mensaje
'''
class Desencriptar_Shamir:

    '''
    Método para desencriptar un mensaje con base a una clave segura utilizando el algoritmo AES.
    @param: Clave segura
    @param: Mensaje
    @return: Criptograma
    '''
    @staticmethod
    def desencriptar_mensaje(clave_segura, mensaje):
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
        iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
        aes = AES.new(key, AES.MODE_CBC, iv)
        encd = aes.encrypt(mensaje)
        print(encd)
    '''
    Método para generar un polonomio a partir de las evaluaciones
    @param: Vector con las evaluaciones en x
    @param: Vector con las evaluaciones en y
    @return: Polinomio resultante de aplicar el método de Interpolación de Lagrange
    '''
    @staticmethod
    def generar_polinomio(x_i, y_i):
        polinomio_lagrange = Lagrange.lagrange(x_i, y_i)
        return polinomio_lagrange.eval(0)

    '''
    Método para desencriptar basado en el esquema Shamir Secret Sharing
    @param: Mensaje a desencriptar
    @param: Evaluaciones
    '''
    def desencriptar(mensaje, x_i, y_i):
        clave_segura = self.generar_polinomio(x_i, y_i)
        mensaje = self.desencriptar_mensaje(clave_segura, mensaje)
        return mensaje 
