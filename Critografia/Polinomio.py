# Biblioteca para trabajar con números aleatorios
import random
# Biblioteca para trabajar con operaciones matemáticas
import math
# Biblioteca para solicitar la contraseña sin tener echo
import getpass
'''
Script ejemplo de manejo de polinomios en python
Implementación de suma de polinomios y multiplicación de polinomios
'''
class Polinomio:
    # Constructor del polinomio
    '''
    Constructor de la clase Polinomio
    @param: Grado del polinomio
    @param: coeficientes (boolean)

        coeficientes = True, se le ingresan los coeficientes del polinomio
        coeficientes = False, se inicializan en cero/aleatoriamente los coeficientes
    @oaram: Array con los coeficientes empezando por [k, x, x^2, ... , x^n]
    '''
    def __init__(self, grado, coeficientes=False, arrCoef=[]):
        # Grado del polinomio

        self.grado = grado

        self.coeficientes = []

        for i in range(0, grado+1):

            if(coeficientes):

                self.coeficientes.append(arrCoef[i])

            else:

                self.coeficientes.append(0)
    # Método para obtener el grado del polinomio
    def getGrado(self):

        return self.grado
    # Método para obtener los coeficientes del polinomio
    def getCoeficientes(self):

        return self.coeficientes
    # Método para obtener el toString del polinomio
    '''
    Los coeficientes empiezan del término independiente hasta el monomio con el exponente del grado
    '''
    def toString(self):

        string = ""

        for i in range(1, self.grado+1):

            string = str(self.coeficientes[i])+"x^"+str(i)+" + " + string

        return string + str(self.coeficientes[0])+"x^"+str(0)

    # Método para multiplicar un polinomio por una constante
    def x(self, constante):

        for i in range(0, self.grado+1):

            self.coeficientes[i] *= constante

    '''
    Método para sumar dos polinomios.
    @param: Polinomio a sumar
    '''
    def add(self, polinomio):

        if(polinomio.getGrado() >= self.grado):

            maximo = polinomio.getCoeficientes()

            minimo = self.coeficientes

        else:

            maximo = self.coeficientes

            minimo = polinomio.getCoeficientes()

        for i in range(0, len(minimo)):

            maximo[i] += minimo[i]
        # Actualizamos las características del polinomio

        self.coeficientes = maximo

        self.grado = len(maximo) - 1

    # Método para multiplicar dos polinomios
    '''
    Me inventé un método en donde se ponen en una matriz de n * m los coeficientes multiplicados
    y luego, al sumar aquellos coeficientes que pertenezcan a la x con el mismo grado, sucede que están
    sobre una misma diagonal, por lo que se implementó un doble for para recaudar la información y sumarla en
    un arreglo final con los coeficientes finales del polonomio.

    @param: Polinomio a multiplicar.
    '''
    def mul(self, polinomio):
        coef1 = self.coeficientes

        coef2 = polinomio.getCoeficientes()

        coefR = []
        # Caso en donde es el polinomio de grado cero
        if(polinomio.getGrado() == 0):

            self.x(coef2[0])

            return
        # Caso en donde este polonomio es el polinomio cero
        if(self.grado == 0):

            polinomio.x(self.coeficientes[0])

            self.grado = polinomio.getGrado()

            self.coeficientes = polinomio.getCoeficientes()

            return
        # Obtenemos el producto de los coeficientes
        for i in range(0, len(coef1)):

            coefR.append([])

            for j in range(0, len(coef2)):

                coefR[i].append(coef1[i] * coef2[j])

        coefP = []
        # Sumamos los primeros coeficientes de las diagonales de toda la matriz
        for i in range(0, polinomio.getGrado()+self.grado+1):

            coefP.append(0)
        # Calculamos la suma de los coeficientes

        soporte = 0

        for i in range(0, len(coef1)):

            indice = soporte

            for j in range(0, len(coef2)):

                coefP[indice] += coefR[i][j]

                indice += 1

            soporte += 1

        self.coeficientes = coefP

        self.grado = polinomio.getGrado() + self.grado

    '''
    Método para evaluar el polinomio en alguna x del dominio real
    @param: número real (x a evaluar)
    @return: P(x)
    '''
    def eval(self, x):

        res = 0

        for i in range(1, len(self.coeficientes)):

            res += self.coeficientes[i] * (x ** i) #  math.pow(x, i)

        return res + self.coeficientes[0]
    '''
    Método para realizar comparación entre polinomios y ver si son iguales
    @param: Polinomio
    @return: True si son iguales, false de lo contrario
    '''
    def equals(self, polinomio):

        if(polinomio.getGrado() != self.grado):

            return False

        coef2 = polinomio.getCoeficientes()

        for i in range(0, len(coef2)):

            if(coef2[i] != self.coeficientes[i]):

                return False

        return True
