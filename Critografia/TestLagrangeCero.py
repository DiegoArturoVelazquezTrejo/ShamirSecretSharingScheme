# Biblioteca para trabajar con números aleatorios
import random
# Biblioteca para trabajar con polonomios
from Polinomio import Polinomio
# Biblioteca para trabajar con el polonomio de Lagrange
from Lagrange import Lagrange
# Biblioteca para trabajar con el polinomio de Lagrange adecuado a este problema
from LagrangeCero import LagrangeCero
# Biblioteca para hacer operaciones sobre el campo Zp
from CampoZP import Zp

# Número primo que utilizaremos para encriptar
campo_zp_primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

grado = 125

# Vamos a generar aleatoriamente xi módulo el primo

zp = Zp(campo_zp_primo)

coeficientes = []

# Agregamos una clave de sha256 como simulacro

coeficientes.append(96509455733429849492299025570430009461567254278459449528478151260985286693756)

for i in range(0, grado):

    coeficientes.append(zp.random_zp(grado))

# Definimos el polinomio

pol = Polinomio(grado, True, coeficientes)

# Ahora aquí vamos a generar los números xi y las evaluaciones

xs = []

ys = []

for i in range(0, grado+1):

    x = zp.random_zp(campo_zp_primo)

    while(x in xs):

        x = zp.random_zp(campo_zp_primo)

    y = pol.eval(x)

    xs.append(x)

    ys.append(y)

#print(int(pol.eval(0)))

#print(pol.toString())

lagrangreP = LagrangeCero(campo_zp_primo)

polinomio_lagrange_cero = lagrangreP.lagrangeCero(xs, ys)

#print(polinomio_lagrange_cero)

if(polinomio_lagrange_cero == pol.eval(0)):
    print("Test Polinomio Interpolación .... 100%")

'''

import sys
    if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
    sys.exit(1)

NUM, MOD = int(sys.argv[1]), int(sys.argv[2])
'''
