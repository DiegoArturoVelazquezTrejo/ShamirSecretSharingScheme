# Biblioteca con algoritmos de hasheo
import hashlib
# Algoritmo para generar la clave segura
from hashlib import sha256
# Biblioteca con los algoritmos de criptografía: algoritmo AES
from Crypto.Cipher import AES
# Biblioteca que contiene al objeto Polinomio
from Polinomio import Polinomio
# Biblioteca para generar números aleatorios
import random
'''
Clase que sigue el esquema Shamir Secret Sharing para encriptar un mensaje
'''
class Encriptar_Shamir:
    '''
    Método para generar la clave segura con base en la contraseña inicial que el usuario ingresa
    @param: clave_usuario (clave que proporciona el usuario)
    @return: clave segura, resultado de aplicar el algoritmo SHA-256 sobre la clave inicial.
    '''
    @staticmethod
    def generar_clave_segura(clave_usuario):
        return sha256(clave_usuario.encode()).hexdigest()

    '''
    Método para encriptar un mensaje con base a una clave segura utilizando el algoritmo AES.
    @param: Clave segura
    @param: Mensaje
    @return: Criptograma
    '''
    @staticmethod
    def encriptar_mensaje(clave_segura, mensaje):
        key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
        iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
        aes = AES.new(key, AES.MODE_CBC, iv)
        encd = aes.encrypt(mensaje)
        print(encd)
    '''
    Método para generar un polonomio aleatoriamente en un campo Zp
    @param: Término independiente del polinomio
    @param: Grado del polinomio
    @return: Polinomio generado
    '''
    @staticmethod
    def generar_polinomio_zp(termino_indep, grado_pol):
        # Número primo que definirá nuestro campo Zp
        campo_zp_primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481
        # Tenemos que generar un polonomio aleatorio con grado_pol coeficientes resultantes de Zp con el primo

        # Regresamos el polinomio
    '''
    Método para encriptar basado en el esquema Shamir Secret Sharing
    @param: Mensaje a encriptar
    @param: Número de personas en total
    @param: Número mínimo de personas para desencriptar
    '''
    def encriptar(mensaje, N, K):
        # Solicitamos la contraseña del usuario
        clave_usuario = input("Ingresa la contraseñ: ")
        # Generamos la contraseña clave_segura
        clave_segura = self.generar_clave_segura(clave_usuario)
        # Generamos el polinomio
        polinomio = generar_polinomio_zp(clave_segura, K)
        # Evaluamos en los N puntos

        # Encriptamos el menaje
        criptograma = self.encriptar_mensaje(clave_segura, mensaje)
        # Regresamos el criptograma y los puntos (evaluacioness)

        return (criptograma)



llave_segura = Encriptar.generar_clave_segura("confidential data")
print(llave_segura)
print(Encriptar.encriptar_mensaje(llave_segura, "HOla como estás?, Esto es confidential"))
