__author__ = 'rick9'
# -*- coding: utf-8 -*-

# Clase de puntajes, inicialmente utilizada. Luego se optó por no usarla
class Puntaje( object ):
    def __init__(self, puntos):
        self.puntos = puntos

    def aumentar(self, puntos , tablero):
        self.puntos += puntos
        self.puntos += filasLlenas(tablero) * 50




def listaPuntajes():
    listaPuntajes = []
    for x in range(4):
        listaPuntajes.append(0)
    return listaPuntajes



def filaLlena(fila):
    llena = True
    for celda in fila:
        if celda == 0:
            llena = False
            break
    return llena

def filasLlenas(tablero):
    numLlenas = 0
    for x in range(0,21):
        if filaLlena(tablero[x]):
            numLlenas += 1
    return numLlenas

# Incrementa puntaje, al final este es el método que se utilizó
def incrementar(puntos , tablero):
    incremento = puntos + filasLlenas(tablero) * 50
    return incremento


