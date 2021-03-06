# -*- coding: iso-8859-15 -*-
#
# VERSION 1.1 (28-Enero-2022)
#
# AYUDA del m?dulo 'modulomatrizasociada'. Define 4 funciones,
# que podemos utilizar de la siguiente forma:
#
# - espaciosVectoriales = leerAplicacionLineal(aplicacionLineal). Lee la aplicaci?n lineal
#   indicada y la devuelve los espacios vectoriales de partida y llegada en una lista
#
# - Base = leerBase(base). Lee la base indicada y devuelve esa misma base en una lista
#
# - leerSolucion(solucion): Lee la solucion con el formato (num1, num2, num3, ...)
#   y crea su correspondiente lista
#
# - transpuesta(matriz): Lee la matriz y calcula su transpuesta
#
# - getFormat

from fractions import Fraction


def leerAplicacionLineal(aplicacion):
    datosApl = aplicacion.split()
    datosApl[0] = datosApl[0][1:-1]
    datosApl[2] = datosApl[2][1:-1]
    Esp1 = datosApl[0].split(",")
    Esp2 = datosApl[2].split(",")
    return [Esp1, Esp2]


def leerBase(base):
    lista = []
    base = base[1:-1]
    base = base.split()
    for i in range(len(base)):
        base[i] = base[i][1:-1]
        vector = base[i].split(",")
        for j in range(len(vector)):
            if not vector[j].isnumeric():
                vector[j] = "(" + str(vector[j]) + ")"
        lista.append(vector)
    return lista


def transpuesta(matriz):
    t = []
    for i in range(len(matriz[0])):
        t.append([])
        for j in range(len(matriz)):
            t[i].append(matriz[j][i])
    return t

def getFormat(solucion):
    solucion = solucion[1:-2]
    datos = solucion.split(",")
    matsol = []
    for i in range(len(datos)):
        unasol = datos[i][1:]
        matsol.append(unasol)
    for elm in range(len(matsol)):
        matsol[elm] = str(Fraction(matsol[elm]).limit_denominator())
    return matsol
