__author__ = 'rick9'
# -*- coding: utf-8 -*-
from operator import itemgetter

#Tipos de piezas de Tetris
#Están dadas por coordenadas representadas por vectores de vectores
#Así es como aparecerán por default, aún no se les hacen rotaciones

#Pieza larga:
I0 = [ [1, 3], [1, 4], [1, 5], [1, 6] ]
I1 = [ [0, 5], [1, 5], [2, 5], [3, 5] ]
I2 = [ [2, 3], [2, 4], [2, 5], [2, 6] ]
I3 = [ [0, 4], [1, 4], [2, 4], [3, 4] ]
I  = [ I0, I1, I2, I3 ]

#Pieza cuadrada:
O0 = [ [0, 4], [0, 5], [1, 4], [1, 5] ]
O1 = [ [0, 4], [0, 5], [1, 4], [1, 5] ]
O2 = [ [0, 4], [0, 5], [1, 4], [1, 5] ]
O3 = [ [0, 4], [0, 5], [1, 4], [1, 5] ]
O  = [ O0, O1, O2, O3 ]

#Pieza L
L0 =  [ [1, 3], [1, 4], [1, 5], [2, 3] ]
L1 =  [ [0, 3], [0, 4], [1, 4], [2, 4] ]
L2 =  [ [1, 3], [1, 4], [1, 5], [0, 5] ]
L3 =  [ [0, 4], [1, 4], [2, 4], [2, 5] ]
L  =  [ L0, L1, L2, L3 ]
#Pieza J
J0 = [ [1, 3], [1, 4], [1, 5], [2, 5] ]
J1 = [ [2, 3], [2, 4], [1, 4], [0, 4] ]
J2 = [ [0, 3], [1, 3], [1, 4], [1, 5] ]
J3 = [ [0, 4], [0, 5], [1, 4], [2, 4] ]
J  = [ J0, J1, J2, J3 ]
#Pieza T
T0 = [ [0, 4], [1, 3], [1, 4], [1, 5] ]
T1 = [ [0, 4], [1, 4], [2, 4], [1, 5] ]
T2 = [ [1, 3], [1, 4], [1, 5], [2, 4] ]
T3 = [ [1, 3], [0, 4], [1, 4], [2, 4] ]
T  = [ T0, T1, T2, T3 ]

#Pieza S
S0 = [ [0, 4], [0, 5], [1, 3], [1, 4] ]
S1 = [ [0, 4], [1, 4], [1, 5], [2, 5] ]
S2 = [ [2, 3], [2, 4], [1, 4], [1, 5] ]
S3 = [ [0, 3], [1, 3], [1, 4], [2, 4] ]
S  = [ S0, S1, S2, S3 ]

#Pieza Z
Z0 = [ [0, 3], [0, 4], [1, 4], [1, 5] ]
Z1 = [ [0, 5], [1, 4], [1, 5], [2, 4] ]
Z2 = [ [1, 3], [1, 4], [2, 4], [2, 5] ]
Z3 = [ [0, 4], [1, 3], [1, 4], [2, 3] ]
Z  = [ Z0, Z1, Z2, Z3 ]

class Pieza( object ):
    def __init__(self, tipo, caidos,coordenadas, rotaciones ):
        self.tipo        = tipo
        self.caidos      = caidos
        self.coordenadas = coordenadas
        self.abajos      = 0 #para el offset de los cuadros
        self.derechas    = 0 #para el offset de los cuadros
        self.rotaciones  = rotaciones

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
        pieza = Pieza(1, 0, I0, I)
    elif valor == 2:
        pieza = Pieza(2, 0, O0, O)
    elif valor == 3:
        pieza = Pieza(3, 0, L0, L)
    elif valor == 4:
        pieza = Pieza(4, 0, J0, J)
    elif valor == 5:
        pieza = Pieza(5, 0, T0, T)
    elif valor == 6:
        pieza = Pieza(6, 0, S0, S)
    elif valor == 7:
        pieza = Pieza(7, 0, Z0, Z)
    return pieza

def reordenar_para_abajo(pieza):
    nuevaPieza = sorted(pieza, key = itemgetter(0))
    nuevaPieza.reverse()
    return (nuevaPieza)

def cambio_nivel(bloque1, bloque2):
    cambio = False
    if(bloque1[0] != bloque2[2]):
        cambio = True
