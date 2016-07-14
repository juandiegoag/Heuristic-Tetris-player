__author__ = 'rick9'
# -*- coding: utf-8 -*-
from operator import itemgetter

#Tipos de piezas de Tetris
#Están dadas por coordenadas representadas por vectores de vectores
#Así es como aparecerán por default, aún no se les hacen rotaciones

#Pieza larga:
I = [ [0, 3], [0, 4], [0, 5], [0, 6] ]

#Pieza cuadrada:
O = [ [0, 4], [0, 5], [1, 4], [1, 5] ]

#Pieza L
L =  [ [0, 3], [0, 4], [0, 5], [1, 3] ]

#Pieza J
J = [ [0, 3], [0, 4], [0, 5], [1, 5] ]

#Pieza T
T = [ [0, 4], [1, 3], [1, 4], [1, 5] ]

#Pieza S
S = [ [0, 4], [0, 5], [1, 3], [1, 4] ]

#Pieza Z
Z = [ [0, 4], [0, 5], [1, 5], [1, 6] ]


class Pieza( object ):
    def __init__(self, tipo, caidos,coordenadas ):
        self.tipo = tipo
        self.caidos = caidos
        self.coordenadas = coordenadas

def setTipo(self, tipo):
    self.tipo = tipo

def getTipo(self):
    return self.tipo

def setCaidos(self, caidos):
    self.tipo = caidos

def getCaidos(self):
    return self.caidos

def setCoordenadas(self,coordenadas):
    self.coordenadas = coordenadas

def getCoordenadas(self):
    return self.coordenadas

def generarPieza(valor):
    pieza = None
    if   valor == 1:
        pieza = Pieza(1, 0, [ [0, 3], [0, 4], [0, 5], [0, 6] ])
    elif valor == 2:
        pieza = Pieza(1, 0, [ [0, 4], [0, 5], [1, 4], [1, 5] ])
    elif valor == 3:
        pieza = Pieza(1, 0, [ [0, 3], [0, 4], [0, 5], [1, 3] ])
    elif valor == 4:
        pieza = Pieza(1, 0, [ [0, 3], [0, 4], [0, 5], [1, 5] ])
    elif valor == 5:
        pieza = Pieza(1, 0, [ [0, 4], [1, 3], [1, 4], [1, 5] ])
    elif valor == 6:
        pieza = Pieza(1, 0, [ [0, 4], [0, 5], [1, 3], [1, 4] ])
    elif valor == 7:
        pieza = Pieza(1, 0, [ [0, 4], [0, 5], [1, 5], [1, 6] ])
    return pieza

def reordenar_para_abajo(pieza):
    nuevaPieza = sorted(pieza, key = itemgetter(0))
    nuevaPieza.reverse()
    return (nuevaPieza)

def cambio_nivel(bloque1, bloque2):
    cambio = False
    if(bloque1[0] != bloque2[2]):
        cambio = True


