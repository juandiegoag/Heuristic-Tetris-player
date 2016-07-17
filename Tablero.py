__author__ = 'rick9'
# -*- coding: utf-8 -*-

import pygame
#Este módulo se encarga de cambios en el tablero y de monitorear su estado

# Revisa que no haya piezas en el tope del tablero, para señalar que la partida sigue
def tableroLleno(tablero):
    lleno = False
    for celda in tablero[2]:
        if celda != 0:
            lleno = True
            break
    return lleno


# Se encarga de eliminar las filas completadas y las sustituye por filas vacías en la parte superior del tablero
def eliminarLlenas(tablero):
    indice = 21
    while indice >= 0:
        if(filaLlena(tablero[indice])):
            nuevaFila = [0] * 10
            tablero.pop(indice)
            tablero.reverse()
            tablero.append(nuevaFila)
            tablero.reverse()
            indice += 1
        indice -= 1


# OTROS METODOS ----------------------------
def filaLlena(fila):
    llena = True
    for celda in fila:
        if celda == 0:
            llena = False
            break
    return llena

def filaVacia(fila):
    vacia = True
    for celda in fila:
        if celda != 0:
            vacia = False
            break
    return vacia
