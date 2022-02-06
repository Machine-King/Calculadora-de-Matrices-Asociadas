# -*- coding: iso-8859-15 -*-
#
# VERSION 1.1 (6-Febrero-2022)
#
# PACKAGES usados:
#   -sympy 1.9
#   -sys
#   -Fraction
# RESOURCES usados:
#   -ModuloMatrices_Aplicaciones.py
# AYUDA del programa MatrizAsociada.p:
#
# El formato a utilizar viene dado al principio. Es IMPORTANTE respetar los espacios para evitar errores

import sys
from ModuloMatrices_Aplicaciones import *
from sympy import symbols, linsolve, Matrix

print("**Bienvenido a Calculadora Avanzada de Matrices Asociadas**")
print("\nFormato introduccion de datos: ")
print("\t-Aplicacion lineal: Cada elemento del espacio de partida y de llegada se separa con una coma (sin espacios)")
print("\t Ejemplo: (x,y,z) -> (x+2*y+z,y,z)\n")
print("\t-Bases: Cada vector de una base se separa con espacios y los elementos de cada vector mediante comas)")
print("\t Ejemplo: {(1,2,3) (1,0,0) (0,0,1)}\n")

aplicacion = input("Introduce la aplicacion f : ")
base1 = input("Introduce una base del (sub)espacio vectorial de partida V : ")
base2 = input("Introduce una base del (sub)espacio vectorial de llegada W : ")
datosApl = leerAplicacionLineal(aplicacion)
Esp1 = datosApl[0]
Esp2 = datosApl[1]
base1 = leerBase(base1)
base2 = leerBase(base2)
matrizAsociada = []
dim_base1 = len(base1)
dim_base2 = len(base2)

for i in range(len(base1)):
    aux = Esp2 + []
    for k in range(len(Esp1)):
        for j in range(len(Esp2)):
            aux[j] = aux[j].replace(Esp1[k], base1[i][k])
    for ecuacion in range(len(aux)):
        aux[ecuacion] = eval(aux[ecuacion])
    matrizAsociada.append(aux)

x, y, z, t = symbols("x, y, z, t")
if dim_base2 == 1:
    parametros = [x]
elif dim_base2 == 2:
    parametros = [x, y]
elif dim_base2 == 3:
    parametros = [x, y, z]
elif dim_base2 == 4:
    parametros = [x, y, z, t]
else:
    sys.exit("No se adminte (sub)espacio de llegada W de dimension mayor a 4")

matrizSol = []
A = Matrix(base2)
for fil in range(len(matrizAsociada)):
    b = Matrix(matrizAsociada[fil])
    solucion = getFormat(str(linsolve((A, b), parametros)))
    matrizSol.append(solucion)

matrizAsociada = transpuesta(matrizSol)


print("\nLa matriz asociada calculada es:")
print("+" + "------------+"*(len(matrizAsociada[0])))
for fila in range(len(matrizAsociada)):
    print("|", end="")
    for col in range(len(matrizAsociada[0])):
        cadena = matrizAsociada[fila][col]
        print(cadena.center(12, " "), end="|")
    print("\n+" + "------------+"*(len(matrizAsociada[0])))
