# Biblioteca para trabajar con los polinomios
from Polinomio import Polinomio
# Biblioteca para generar números aleatorios
import random
'''
 Pruebas de la clase Polinomio
'''
class TestPolinomios:
    '''
    Método para hacer test sobre la operación de suma de polinomios
    '''
    def testSumaPolinomios(self):
        coeficientes_1 = []
        coeficientes_2 = []

        grado_1 = random.randint(0, 20)
        grado_2 = random.randint(0, 20)

        for i in range(0, grado_1+1):
            coeficientes_1.append(random.randint(0,20))
        for i in range(0, grado_2+1):
            coeficientes_2.append(random.randint(0,20))

        pol_1 = Polinomio(grado_1, True, coeficientes_1)
        pol_2 = Polinomio(grado_2, True, coeficientes_2)

        if(grado_1 >= grado_2):
            min = grado_2
            pol_grande = coeficientes_1
            pol_chico  = coeficientes_2
        else:
            min = grado_1
            pol_chico = coeficientes_1
            pol_grande  = coeficientes_2

        for i in range(0, min+1):
            pol_grande[i] = pol_grande[i] + pol_chico[i]

        pol_suma = Polinomio(len(pol_grande)-1, True, pol_grande)


        pol_1.add(pol_2)

        if(pol_1.equals(pol_suma)):
            print("Test Suma de Polinomios   ....   100%")
        else:
            print("Error en Test de Suma de Polinomios")

    '''
    Método para hacer test sobre la operación de multiplicación por un escalar
    '''
    def testProductoEscalar(self):
        coeficientes_1 = []

        grado_1 = random.randint(0, 20)

        for i in range(0, grado_1+1):
            coeficientes_1.append(random.randint(0,20))

        pol_1 = Polinomio(grado_1, True, coeficientes_1)

        c = random.randint(0, 20)

        pol_1.x(c)

        for i in range(0, grado_1+1):
            coeficientes_1[i] *= c

        pol_prod = Polinomio(grado_1, True, coeficientes_1)

        if(pol_prod.equals(pol_1)):
            print("Test Producto por Escalar  ....  100%")
        else:
            print("Error en Test de Producto Escalar ")

    '''
    Método para hacer test sobre la operación de multiplicación por un polonomio
    '''
    def testProductoPolinomial(self):
        pol_1 = Polinomio(1, True, [1, 1]) # x + 1

        pol_aux = Polinomio(1, True, [1, 1]) # x + 1

        coeficientes_pascal = [[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1]]

        for i in range(0, 7):
            if(not self.igualdad_listas(coeficientes_pascal[i], pol_1.getCoeficientes())):
                print("Error en producto polinomial ")

            pol_1.mul(pol_aux)

        print("Test de Producto Polinomial .... 100% ")
    '''
    Método auxiliar para verificar igualdad en listas
    '''
    def igualdad_listas(self, lista1, lista2):
        if(len(lista1) != len(lista2)):
            return False

        for i in range(0, len(lista1)):
            if(lista1[i] != lista2[i]):
                return False
        return True
    '''
    Método para hacer test sobre la evaluación de un polonomio
    '''
    def testEvaluacionPolinomio(self):
        pol_1 = Polinomio(1, True, [1, 1]) # x + 1
        
        pol_aux = Polinomio(1, True, [1, 1]) # x + 1

        coeficientes_pascal_suma = [2, 4, 8, 16, 32, 64, 128, 256, 512] # del grado 0 al 9

        for i in range(0, 9):
            if(pol_1.eval(1) != coeficientes_pascal_suma[i]):
                print("Error en prueba de evaluación ")
            pol_1.mul(pol_aux)

        print("Test de evaluación en un x  .... 100% ")

    '''
    Método que realiza todas las pruebas
    '''
    def test(self):
        self.testSumaPolinomios()
        self.testProductoEscalar()
        self.testEvaluacionPolinomio()
        self.testProductoPolinomial()

# Creamos una instancia de la clase test
test = TestPolinomios()
# Realizamos las pruebas unitarias
test.test()
