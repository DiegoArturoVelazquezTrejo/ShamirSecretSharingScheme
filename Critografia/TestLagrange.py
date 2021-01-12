# Pruebas unitarias para el polinomio de interpolación de Lagrange
class TestPolinomios:
    '''
    Método para verificar la eficiencia del método de interpolación de Lagrange
    '''
    @staticmethod
    def test_vectors():
        c_p = random.randint(0,20)
        puntos_x = [] # Arreglo con las coordenadas en X
        puntos_y = [] # Arreglo con las coordenadas en Y
        for i in range(0, c_p):
            puntos_x.append(random.randint(0, 1000))
            puntos_y.append(random.randint(0, 1000))
        lagrange = Lagrange()
        pol_lag  = lagrange.lagrange(puntos_x, puntos_y)

        # Ahora verificaremos que las imágenes correspondan a las X dadas
        for i in range(0, len(puntos_x)):
            eval_y = pol_lag.eval(puntos_x[i])
            if(eval_y != puntos_y[i]):
                print(pol_lag.toString())
                print("Error en evaluación:  P(xi) = "+str(eval_y)+"   , yi = "+str(puntos_y[i]))
                return
        print("Prueba unitaria del polinomio de extrapolación de Lagrange ....... 100%")

TestPolinomios.test_vectors()
