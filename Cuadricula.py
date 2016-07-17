__author__ = 'rick9'
# -*- coding: utf-8 -*-

import pygame
import sys
from Movimientos import *
from Tablero import *
from Piezas import *
from Puntaje import *
from Jugadas import evaluarJugadas
from Evolucion import *
from random import randint


import time
import threading


# Definición de constantes
# COLORES---------------------------------------------------
# Fondos
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = 	(6, 6, 6)

# Colores piezas, uno para cada tipo
AZUL =	(0, 0, 255)
ROJO = (255, 0, 0)
MAGENTA = (208, 32, 144)
CYAN = (0, 206, 209)
AMARILLO = (255, 255, 0)
LIMA = (50, 205, 50)
NARANJA = (255, 140, 0)
#DIMENSIONES ---------------------------------------------
# Establecemos el LARGO y ALTO de cada celda de la pantalla.
LARGO  = 20
ALTO = 20
# Establecemos el margen entre las celdas.
MARGEN = 2


#INICIALIZACIONES ----------------------------------------
# Inicializamos pygame
pygame.init()
# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [1032, 492]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la pantalla.
pygame.display.set_caption("Tetris Algoritmo Genético")

# Reloj para marcar el tiempo de refrescamiento de la pantalla
reloj = pygame.time.Clock()




# Recibe una matriz (lista de listas) de enteros y a partir de los valores
# dibuja el tablero en cada iteración usando el método draw.rect de pygame
# el color de cada celda depende del tipo de pieza en el tablero
def dibujar(grid, offset):
    for fila in range(22):
        for columna in range(10):
            color = NEGRO
            if grid[fila][columna]   == 1:
                color = CYAN
            elif grid[fila][columna] == 2:
                color = MAGENTA
            elif grid[fila][columna] == 3:
                color = ROJO
            elif grid[fila][columna] == 4:
                color = LIMA
            elif grid[fila][columna] == 5:
                color = AMARILLO
            elif grid[fila][columna] == 6:
                color = NARANJA
            elif grid[fila][columna] == 7:
                color = AZUL
            if fila == 0 or fila == 1:
                color = GRIS

            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN + 260 * offset,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])


# Retorna cuatro tableros nuevos inicializados en 0
def listaTableros():
    lista = []
    for x in range(4):
        tablero = []
        for fila in range(22):
            tablero.append([])
            for columna in range(10):
                tablero[fila].append(0) # Añade una celda
        lista.append(tablero)
    return lista


# Método más importante, se encarga de ejecutar una corrida de Tetris
def juego(grid, offset, gen, puntaje):
    finCaida = False
    # Se genera pieza aleatoria de Tetris
    pieza = generarPieza(randint(1,7))

    #Hace un número aleatorio de rotaciones  a la pieza
    for x in range(0, randint(0,4)):
        pieza = rotarDerecha(grid,22,10,pieza)

    # Muy importante: evalúa la pieza actual y simula las posibles jugadas, la más efectiva según los pesos actuales de cada
    # heurística definirá el número de desplazamientos a realizar
    movimientos = evaluarJugadas(grid, pieza, gen)

    # Si son positivos se mueve hacia la derecha, si no hacia la izquierda, si es 0 no se mueve
    if(movimientos[1] > 0):
        for x in range(0, movimientos[1]):
            desplazarDerecha(grid,pieza)
    elif movimientos[1] < 0:
        for x in range(0, - movimientos[1]):
            desplazarIzquierda(grid, pieza)

    # Reordena para que la pieza caiga en orden correcto, de lo contrario se deforma
    pieza.coordenadas = reordenar_para_abajo(pieza.coordenadas)

    # Ciclo de caída de pieza termina cuando la pieza toca el piso o choca con otra
    # En cada iteración se actualiza el grid y se dibuja nuevamente

    while not finCaida:
        finCaida = caidaPieza(grid, 22, 10, pieza)
        dibujar(grid, offset)
        pygame.display.flip()
        #Define la velocidad de la animación
        reloj.tick(20)
    # Se suma al puntaje: 18 por pieza mas 50 por fila llena en el grid
    puntaje += incrementar(18, grid)
    # Si al final de la caída de una pieza se llena alguna línea entonces se elimina
    eliminarLlenas(grid)

    # Si se llena el tablero entonces este se reinicia llenandolo con 0s para la siguiente partida
    if(tableroLleno(grid)):


        del grid[:]
        for fila in range(22):
        # Añadimos un array vacío que contendrá cada celda
        # en esta fila
            grid.append([])
            for columna in range(10):
                grid[fila].append(0) # Añade una celda


# Método más importante que inicializará variables globales para los hilos
# Llama a los hilos
def main():

    # Se crean los tableros para cada hilo, 4 en total
    tableros = listaTableros()
    pantalla.fill(GRIS)

    # Inicializa una generación de genes aleatorios, cada uno corresponde a un peso para cada heurística
    genes = listaGenes()
    # Inicializa puntajes para cada hilo
    puntajes = listaPuntajes()

    # booleano que controla el ciclo principal
    corriendo = True
    generaciones = 1
    while corriendo: # Ciclo principal
        for evento in pygame.event.get(): # Eventos de pygame, no usados pero necesarios manejarlos para que el programa corra
            if evento.type == pygame.QUIT:
                corriendo = False

        # Se crean cuatro hilos para que cada uno se encarge de cada partida en cada generación
        t1 = threading.Thread(target=juego, args=(tableros[0],0,genes[0],puntajes[0],))
        t2 = threading.Thread(target=juego, args=(tableros[1],1,genes[1],puntajes[1],))
        t3 = threading.Thread(target=juego, args=(tableros[2],2,genes[2],puntajes[2],))
        t4 = threading.Thread(target=juego, args=(tableros[3],3,genes[3],puntajes[3],))

        # Se corren hilos
        t1.start()
        t2.start()
        t3.start()
        t4.start()

        # join a cada hilo
        t1.join(10)
        t2.join(10)
        t3.join(10)
        t4.join(10)

        # Con base en los resultados de cada corrida se crea una nueva generación de genes modificando la lista "genes"
        # Esta lista irá "evolucionada" a la siguiente iteración
        nuevaGeneracion(genes, puntajes)
        generaciones += 1


   #nuevaGeneracion(genes, puntajes)

main()

# Llamado para terminar pygame
pygame.quit()

