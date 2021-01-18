
# Biblioteca para trabajar con CampoZp
from CampoZP import Zp
# Biblioteca para trabajar con números aleatorios
import random

'''
Pruebas unitarias para la clase CampoZp
'''

class TestCampoZp:
    # Constructor de la clase
    def __init__(self):
        self.p = 208351617316091241234326746312124448251235562226470491514186331217050270460481

        self.zp = Zp(self.p)
    # Método para testear la suma cerrada bajo el campo
    def testSuma(self):
        for i in range(0, 100):

            a = self.zp.random_zp(self.p)

            b = self.zp.random_zp(self.p)

            suma = a + b

            suma = self.zp.suma(a, b)

            if(suma != (suma % self.p)):

                print("Error en test suma ... ")

        print("Test suma en campoZp  .... 100% ")

    # Método para probar el producto cerrado bajo el campo
    def testProducto(self):
        for i in range(0, 100):

            a = self.zp.random_zp(self.p)

            b = self.zp.random_zp(self.p)

            prodN = a * b

            prod = self.zp.producto(a, b)

            if(prod != (prodN % self.p)):

                print("Error en test producto ... ")

        print("Test producto en campoZp  .... 100% ")

    # Método para probar el inverso bajo el campo
    def testInverso(self):
        for i in range(0, 100):

            a = self.zp.random_zp(self.p)

            b = self.zp.inverso(a)

            if(self.zp.producto(a, b) != 1):

                print("Error en test inverso multiplicativo ... ")

        print("Test inverso multiplicativo en campoZp  .... 100% ")

    # Método para probar la equivalencia (clases de equivalencia)
    def testEquivalencia(self):

        zp1 = Zp(13)

        for i in range(0, 100):

            a = random.randint(0, 100)

            equiv = zp1.equivalencia(a)

            residuo = a % 13

            if(residuo != equiv):

                print("Error en test equivalencia ... ")

        print("Test suma en equivalencia  .... 100% ")
    # Método para probar el generador de números aleatorios
    def testRandomNumbers(self):

        zp1 = Zp(17)

        for i in range(0, 100):

            a = zp1.random_zp(100)

            if(a >= 17):

                print("Error en test de números aleatorios en Zp  ... ")

        print("Test de números aleatorios bajo Zp .... 100% ")

    # Método que agrupa todas las pruebas
    def test(self):

        self.testSuma()

        self.testInverso()

        self.testProducto()

        self.testRandomNumbers()

        self.testEquivalencia()


pr = TestCampoZp()

pr.test()
