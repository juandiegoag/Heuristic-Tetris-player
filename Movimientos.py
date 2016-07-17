__author__ = 'rick9'
# -*- coding: utf-8 -*-

from Tablero import filaVacia

import pygame
import copy
# Este módulo se encarga del movimiento de piezas en el tablero incluyendo caídas, movimientos laterales y rotaciones

def caidaPieza(tablero, dimension_x, dimension_y, pieza):

    fin = False
    fondo  = dimension_x
    indice = 0
    i      = 0
    tocarFondo = colisionAbajo(pieza, dimension_x, dimension_y, tablero)
    if(tocarFondo): pieza.caidos += 1
    if(pieza.caidos >= 4): fin = True


    for bloque in pieza.coordenadas:
        coordenadaX = bloque[0]
        coordenadaY = bloque[1]
        i           +=1

        if coordenadaX + 1 < fondo:
            if not tocarFondo: tablero[coordenadaX][coordenadaY] = 0
            coordenadaX        = coordenadaX + 1
            bloque[0]          = coordenadaX
            if not tocarFondo: tablero[coordenadaX][coordenadaY] = pieza.tipo
    if not tocarFondo: pieza.abajos += 1
    return fin

def colisionAbajo(pieza, dimension_x,dimension_y, tablero):
    tocarFondo = False
    r = []
    for i in pieza.coordenadas:
        if [i[0] + 1, i[1]] not in pieza.coordenadas:
            r.append(i)

    for bloque in r:
        if bloque[0] == dimension_x - 1 or tablero[ bloque[0] + 1 ][ bloque[1] ] != 0:
            tocarFondo = True
            break
    return tocarFondo

def puedeMoverIzquierda(tablero, pieza):
    puedo = True
    r = []

    for i in pieza:
        if i[1] < 0: return False
        if [i[0], i[1] - 1] not in pieza:
            r.append(i)
    for bloque in r:
        if i[1] < 0: return False
        if bloque[1] == 0 or tablero[ bloque[0] ][ bloque[1] - 1 ] != 0:
            puedo = False
            break
    return puedo

def desplazarIzquierda(tablero, pieza):
    if puedeMoverIzquierda(tablero, pieza.coordenadas):
        sorted(pieza.coordenadas, key = lambda x: x[1])
        for bloque in pieza.coordenadas:
            tablero[ bloque[0] ][ bloque[1] ] = 0
            bloque [1] -= 1
            pieza.derechas -= 1
    return pieza



def puedeMoverDerecha(tablero, pieza):
    puedo = True
    r = []
    for i in pieza:
        if [i[0], i[1] + 1] not in pieza:
            r.append(i)
    for bloque in r:
        if bloque[1] == 9 or tablero[ bloque[0] ][ bloque[1] + 1 ] != 0:
            puedo = False
            break
    return puedo

def desplazarDerecha(tablero, pieza):
    if puedeMoverDerecha(tablero, pieza.coordenadas):
        sorted(pieza.coordenadas, key = lambda x: x[1])
        for bloque in pieza.coordenadas:
            tablero[ bloque[0] ][ bloque[1] ] = 0
            bloque [1] += 1
            pieza.derechas += 1
    return pieza


def borrarPieza(tablero, pieza):
    for bloque in pieza.coordenadas:
        tablero[ bloque[0] ][ bloque[1] ] = 0


def pintarPieza(tablero, pieza):
    for bloque in pieza.coordenadas:
        tablero[ bloque[0] ][ bloque[1] ] = pieza.tipo

def rotarDerecha(tablero, dimension_x, dimension_y, pieza):
    nuevaPieza             = copy.deepcopy(pieza)
    nuevaPieza.coordenadas = puedeRotarDerecha(tablero, dimension_x, dimension_y, pieza)
    if not nuevaPieza.coordenadas:
        nuevaPieza = pieza
    else:
        borrarPieza(tablero,pieza)
        pintarPieza(tablero,nuevaPieza)
    return nuevaPieza

def puedeRotarDerecha(tablero, dimension_x, dimension_y, pieza):
    piezaNueva = copy.deepcopy(pieza)
    if colisionAbajo(pieza, dimension_x, dimension_y, tablero) : return []
    if pieza.abajos < 0 : return []
    if pieza.abajos > dimension_x - 1 or pieza.derechas < -4 or pieza.derechas > dimension_y - 1:
        return []
    piezaNueva.coordenadas[:] = [ [x[0] - pieza.abajos, x[1] - pieza.derechas] for x in piezaNueva.coordenadas[:] ]
    piezaNueva.coordenadas    = siguienteRotacionDerecha(piezaNueva)
    piezaNueva.coordenadas[:] = [ [x[0] + pieza.abajos, x[1] + pieza.derechas] for x in piezaNueva.coordenadas[:] ]

    r    = []
    for i in piezaNueva.coordenadas:
        if [i[0], i[1]] not in pieza.coordenadas:
            r.append(i)
    for i in r:
        if tablero[ i[0] ][ i[1] ] != 0:
            return []
    return piezaNueva.coordenadas


def siguienteRotacionDerecha(pieza): #recibe la pieza, devuelve el offset de la siguiente rotacion
    i = 0
    for opciones in pieza.rotaciones:
        if sorted(opciones) == sorted(pieza.coordenadas):
            if i != 3: return pieza.rotaciones[i + 1]
            else     : return pieza.rotaciones[  0  ]
        i += 1
    return pieza.coordenadas