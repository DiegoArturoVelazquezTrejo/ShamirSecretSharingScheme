# Biblioteca para trabajar con operaciones matemáticas
import math
# Biblioteca para trabajar con números aleatorios
import random

# Clase que modela los métodos necesarios para operar números bajo un Zp en donde p será un primo para este proyecto y así garantizar que es campo.
class Zp:
    # Constructor de la clase Zp,
    # @param: p donde p es un número entero.
    def __init__(self, p):
        # Verificamos que el número sea distinto de 0
        if(p == 0):

            print(" Ingrese un número distinto de cero ... ")

            self.p = int(input())

            while(self.p == 0):

                self.p = int(input())

        else:

            self.p = p

    '''
    Suma cerrada bajo el campo Zp
    @param: N entero
    @param: M entero
    @return: N + M bajo el campo Zp
    '''
    def suma(self, N, M):

        return (N + M) % self.p
    '''
    Método de producto bajo el campo Zp
    @param: N entero
    @param: M entero
    @return: (N * M) bajo el campo Zp
    '''
    def producto(self, N, M):

        return (N * M) % self.p
    '''
    Método para obtener el inverso multiplicativo de un número en Zp
    @param: N entero
    @return: M entero en Zp tal que N * M = 1
    '''
    def inverso(self, num):
        if(num == 0):

            return 0
        if(num == 1):

            return 1
        '''
        This function uses ordinary integer arithmetic implementation of the
        Extended Euclid’s Algorithm to find the MI of the first-arg integer
        vis-a-vis the second-arg integer.

        Fuente del algoritmo: Theoretical Underpinnings of Modern Cryptography, by Avi Kak (kak@purdue.edu). May 7, 2020

        '''
        mod = self.p

        NUM = num; MOD = self.p

        x, x_old = 0, 1

        y, y_old = 1, 0

        while mod:

            q = num // mod

            num, mod = mod, num % mod

            x, x_old = x_old - q * x, x

            y, y_old = y_old - q * y, y

        if num != 1:

            print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, MOD, num))

        else:

            MI = (x_old + MOD) % MOD
            #print("\nMI of %d modulo %d is: %d\n" % (NUM, MOD, MI))
            return MI
    '''
    Método para asignarle la clase de equivalencia correspondiente a cualquier número entero
    @param: N entero
    @return: N % p
    '''
    def equivalencia(self, N):

        return N % self.p
    '''
    Método para generar números aleatorios bajo el campo Zp
    @param: Límite superior del generador de números aleatorios
    @return: Número aleatorio dentro de Zp
    '''
    def random_zp(self, limite):

        return random.randint(0, limite) % self.p

# Algunas pruebas
'''
p = 17

zp = Zp(p)

elementos = [i for i in range(1, p)]

for i in range(0, len(elementos)):

    print(" El elemento "+str(elementos[i]) + " tiene como inverso a "+str(zp.inverso(elementos[i]))+" y el producto es: "+str(zp.producto(zp.inverso(elementos[i]), elementos[i])))
'''
