__author__ = 'rick9'
# -*- coding: utf-8 -*-
import pygame
# Se usará este módulo para realizar modificaciones sobre la matriz de valores
def puedeMoverIzquierda(tablero, pieza):
    puedo = True
    r = []
    for i in pieza:
        if [i[0], i[1] - 1] not in pieza.coordenadas:
            r.append(i)
    for bloque in r:
        if bloque[1] == 0 or tablero[ bloque[0] ][ bloque[1] - 1 ] != 0:
            puedo = False
            break
    return puedo

def desplazarIzquierda(tablero, pieza):
    ordenadoY = pieza.coordenadas
    if puedeMoverIzquierda(tablero, pieza.coordenadas):
        ordenadoY = sorted(pieza.coordenadas, key = lambda x: x[1])
        for bloque in ordenadoY:
            tablero[ bloque[0] ][ bloque[1] ] = 0
            bloque [1] -= 1
            ordenadoY.derechas -= 1
    return ordenadoY

def puedeMoverDerecha(tablero, dimension_y, pieza):
    puedo = True
    r = []
    for i in pieza.coordenadas:
        if [i[0], i[1] + 1] not in pieza.coordenadas:
            r.append(i)
    for bloque in r:
        if bloque[1] == dimension_y - 1 or tablero[ bloque[0] ][ bloque[1] + 1 ] != 0:
            puedo = False
            break
    return puedo

def desplazarDerecha(tablero, dimension_y, pieza):
    ordenadoY = pieza
    if puedeMoverDerecha(tablero, dimension_y, pieza.coordenadas):
        ordenadoY = sorted(pieza.coordenadas, key = lambda x: x[1])
        ordenadoY = ordenadoY[::-1]
        # print ordenadoY
        for bloque in ordenadoY:
            tablero[ bloque[0] ][ bloque[1] ] = 0
            bloque [1] += 1
            ordenadoY.derechas += 1
    return ordenadoY

# def puedeRotarDerecha(tablero, pieza, dimension_x, dimension_y):
#     piezaNueva  = pieza
#     if pieza.abajo > dimension_x - 1 or pieza.derechas < 0 or pieza.derechas > dimension_y - 1:
#         return False
#
#     #obtener siguiente pieza en rotaciones
#     #hacer pieza nueva la siguiente rotacion y sumar los offsets a todos
#
#     r = []
#     for i in piezaNueva.coordenadas:
#         if [i[0] + 1, i[1]] not in pieza.coordenadas:
#             r.append(i)
#     for i in r
#         if tablero[ i[0] ][ i[1] ] != 0:
#             return False
#     return True

def caidaPieza(tablero, dimension_x, dimension_y, pieza):
    fin = False
    fondo  = dimension_x
    indice = 0
    tocarFondo = colisionAbajo(pieza, dimension_x, dimension_y, tablero)
    if(tocarFondo): pieza.caidos += 1
    # print(pieza.caidos)
    if(pieza.caidos >= 4): fin = True
    for bloque in pieza.coordenadas:
        coordenadaX = bloque[0]
        coordenadaY = bloque[1]
        if coordenadaX + 1 < fondo:
            if not tocarFondo: tablero[coordenadaX][coordenadaY] = 0
            coordenadaX        = coordenadaX + 1
            bloque[0]          = coordenadaX
            if not tocarFondo:
                tablero[coordenadaX][coordenadaY] = 2
                pieza.abajos += 1
        indice = indice + 1
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
