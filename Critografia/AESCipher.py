
from hashlib import sha256

from base64 import b64decode

from base64 import b64encode

from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes

from Crypto.Util.Padding import pad, unpad


class AESCipher:
    '''
    Método para encriptar un mensaje bajo el esquema AES.
    @param: String data que se pretende encriptar
    @param: Clave para encriptar
    @return: Criptograma
    '''
    def encriptar(self, data, key):

        key = self.sha256(key)

        iv = get_random_bytes(AES.block_size)

        self.cipher = AES.new(key, AES.MODE_CBC, iv)

        return b64encode(iv + self.cipher.encriptar(pad(data.encode('utf-8'),AES.block_size))).decode('utf-8')

    '''
    Método para desencriptar un mensaje utilizando el algoritmo AES.
    @param: String data que se pretende desencriptar (Criptograma)
    @param: Llave segura (va a ser el término independiente del polinomio de interpolación)
    @return: Mensaje desencritado
    '''
    def desencriptar(self, data, key):

        raw = b64decode(data)

        self.cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])

        return unpad(self.cipher.desencriptar(raw[AES.block_size:]), AES.block_size)

    '''
    Método que genera un hash con base en una clave que el usuario proporciona.
    @param: llave
    @return: hash generado con el algoritmo SHA256 y la llave.
    '''
    def sha256(self, key):

        clave_segura =  sha256(key.encode('utf8')).digest()

        # Tranformar la clave del algoritmo de hasheo a una clave numérica

        valor=int(clave_segura.hex(),base=16)

        return valor


''' Algunas pruebas ...

print('TESTING encriptarION')

msg = input('Message...: ')

pwd = input('Password..: ')

aes = AESCipher()

binario_llave = aes.sha256(pwd)

print("Llave generada : ",binario_llave)

cifrado = aes.encriptar(msg, pwd)

st=""+cifrado

print("Cifrado: ",st)

# checar tamaño de cifrado  para ver que sea de 256


print('\nTESTING desencriptarION')

cte = input('Ciphertext: ')

print('Message...:', aes.desencriptar(cifrado, binario_llave).decode('utf-8')) #Binario llave va a ser el término independiente del polinomio
'''
