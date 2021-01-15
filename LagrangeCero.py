# Biblioteca para manejar los polonomios
from Polinomio import Polinomio
# Biblioteca para trabajar decimales
from decimal import *
# Biblioteca para trabajar con el campo Zp
from CampoZP import Zp

# Clase que implementa la elaboración de la extrapolación de Lagrange
class LagrangeCero:
    # Constructor de la clase polonomio cero lagrange en Zp
    # @param: p entero del campo Zp donde se trabajará el polonomio
    def __init__(self, p):

        self.zp = Zp(p)

    '''
    Método para obtener los Li de la ecuación del método de interpolación de Lagrange
    @param: x_i
    @param: array coeficientes en X
    @return: Polinomio Li(x)
    '''
    def li(self, i_i, coeficientes_x):

        denominador = 1

        numerador = 1

        for j in range(0, len(coeficientes_x)):

            if(int(coeficientes_x[j]) != int(i_i)):

                numerador *= int(-coeficientes_x[j])

                denominador *= int(i_i-coeficientes_x[j])

        numerador = self.zp.equivalencia(numerador)

        denominador = self.zp.equivalencia(denominador)

        denominador = self.zp.inverso(denominador)

        return self.zp.producto(numerador, denominador)
    '''
    Método principal para el polinomio de Lagrange
    @param: vector con las x_i
    @param: vector con las y_i
    @return: Polinomio de lagrange generado por la intepolación
    '''
    def lagrangeCero(self, x_i, y_i): # vectores = [(0, 1), (1, 3), (2, 0)]
        suma = 0

        for i in range(0, len(x_i)):

            pol = self.li(x_i[i], x_i)

            producto = self.zp.producto(pol, self.zp.equivalencia(y_i[i])) # f(xi) * Li(x = 0)

            suma += producto

        return int(self.zp.equivalencia(suma))
