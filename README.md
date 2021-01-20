# Proyecto de Cifrado que implementa el Esquema de Shamir Sharing Secret
----
# Universidad Nacional Autónoma de México

## Facultad de Ciencias

### Ciencias de la Computación

----
Autores: Diego Arturo Velázquez Trejo (https://github.com/DiegoArturoVelazquezTrejo)
Mario Escobar Rosales (https://github.com/luismarioescobarrosales2000)
========================

#### Descripción:
  - Se desarrolló un sistema que encripta mensajes con base en el sistema de Shamir: https://es.wikipedia.org/wiki/Esquema_de_Shamir.

  El esquema Shamir Sharing Secret consiste en encriptar información y entregar una cierta cantidad (N) de claves a los participantes.
  Cuando se desee descifrar la información, de los N participantes, se tienen que juntar K (K <= N) participantes y proporcionar su share que consiste en dos números (entregados por el sistema después de encriptar).
  En caso que los números no hayan sido modificados y en efecto sean K personas, el mensaje se podrá descifrar, de lo contrario, no se podrá.

  Tanto N como K los especifica el usuario antes de encriptar. Véase el apartado de ejecución del programa.

### Requisitos para la ejecución correcta del programa:

  1) Versión Python3.0.0 en adelante
  2) Biblioteca hashlib
  3) Biblioteca b64encode
  4) Biblioteca Cypto.Cipher
  5) Biblioteca Cypto.Random
  6) Biblioteca Cypto.Util.Padding
  7) Biblioteca docx
  8) Biblioteca textract
  9) Biblioteca fpdf

  Lo anterior se resume a teclear en la consola:
  ```
  $ pip install pycryptodome
  $ pip3 install pycryptodome

  $ pip install docx
  $ pip3 install docx

  $ pip install textract
  $ pip3 install textract

  $ pip install fpdf
  $ pip3 install fpdf

  ```
  Dependiendo la versión de pip.

### Para ejecutar el CIFRADO:
```
$ python3 Main.py -c claves N K mensaje

Donde claves es un archivo donde se guardarán las claves para descifrar la información.
N es el número de personas que participarán en el desencriptado de la información.
K es el número mínimo de personas que se requieren juntar para descifrar el archivo.
mensaje que es el nombre de un archivo dentro de la misma carpeta que contiene la información que se encriptará.
```
### Para ejecutar el DESENCRIPTADO:
```
$ python3 Main.py -d claves mensaje

Donde claves es el archivo donde están guardadas las claves  
mensaje que es el nombre de un archivo dentro de la misma carpeta que contiene el criptograma.

```

### Observaciones y proceso de análisis:

  Se diseñó una biblioteca para trabajar con polinomios (contiene operaciones de suma, producto por escalar, producto por polinomio y evaluación) ya que el esquema de Shamir hace uso del espacio vectorial de polinomios. Cabe mencionar, que esta biblioteca se puede usar con otros fines (no se limita a este proyecto).
  También se implementó una clase para trabajar con los Polinomios de Interpolación de Lagrange ya que cuando se generan los shares para los participantes,
  estas son de la forma (X, P(X)), donde P(X) es un polinomio aleatorio que se genera cuando se encripta la información. El grado del polinomio es K-1, de ahí resulta
  que se requieren al menos K participantes para recontruir el polinomio. El arhivo Lagrange.py es un archivo que realiza una interpolación de polinomios sin evaluar en el punto cero, por lo que también puede ser utilizada como biblioteca para otros fines ajenos a los de este proyecto.

  Una vez que se recontruyó el polinomio, la evaluación en 0 implica que obtenemos el término independiente que
  coincide con la clave de hasheo que el sistema utilizó para encriptar la información.

  También se diseñó una clase Zp ya que toda operación que el sistema realiza está cerrada bajo Zp donde p es un primo muy grande. Esto con la finalidad de deshacernos de las fracciones
  en el polinomio de interpolación y de trabajar con los números reales, perdiendo presición. Como Zp tiene a p primo, todos los elementos van a tener inverso multiplicativo, y así eliminamos el
  trabajo con números de punto flotante o doubles y trabajamos con puros números enteros.

### Para ejecutar pruebas unitarias:
 ```
 $ python3 NombreDeLaPruebaUnitaria.py

 ```
