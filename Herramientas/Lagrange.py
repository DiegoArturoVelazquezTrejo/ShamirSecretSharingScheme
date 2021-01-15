# Biblioteca para manejar los polonomios
from Polinomio import Polinomio
# Biblioteca para trabajar decimales
from decimal import *
# Clase que implementa la elaboración de la extrapolación de Lagrange
class Lagrange:
    '''
    Método para obtener los Li de la ecuación del método de interpolación de Lagrange
    @param: x_i
    @param: array coeficientes en X
    @return: Polinomio Li(x)
    '''
    def li(self, i_i, coeficientes_x):

        denominador = 1

        polF = Polinomio(0, True, [1, 0]) # polF(x) = 1

        # Quitar de coeficientes_x el elemento i_i

        lista_denominadores = []

        for j in range(0, len(coeficientes_x)):

            if(coeficientes_x[j] != i_i):

                pol = Polinomio(1, True, [-coeficientes_x[j], 1]) # (x - xi)

                polF.mul(pol) # (x - xi) (x - xi+1) ... (x - xn)

                # Me falta el denominador que es xi - xj

                denominador = denominador * (1/(i_i-coeficientes_x[j]))

                lista_denominadores.append((1, i_i - coeficientes_x[j]))

        polF.x(denominador)

        return polF
    '''
    Método principal para el polinomio de Lagrange
    @param: vector con las x_i
    @param: vector con las y_i
    @return: Polinomio de lagrange generado por la intepolación
    '''
    def lagrange(self, x_i, y_i): # vectores = [(0, 1), (1, 3), (2, 0)]

        polF = Polinomio(0, True, [0, 0]) # polF(x) = 0

        for i in range(0, len(x_i)):

            pol = self.li(x_i[i], x_i)

            pol.x(y_i[i])    # f(xi) * Li(x)

            polF.add(pol)

        return polF
