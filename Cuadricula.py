__author__ = 'rick9'
# -*- coding: utf-8 -*-

import pygame
from Tablero import *
from Piezas import *
from random import randint

# Definición de constantes
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

AZUL =	(0, 0, 255)
ROJO = (255, 0, 0)
MAGENTA = (208, 32, 144)
CYAN = (0, 255, 255)
AMARILLO = (255, 255, 0)
LIMA = (50, 205, 50)
NARANJA = (255, 140, 0)

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO  = 20
ALTO = 20

# Establecemos el margen entre las celdas.
MARGEN = 2

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
grid = []
for fila in range(22):
    # Añadimos un array vacío que contendrá cada celda
    # en esta fila
    grid.append([])
    for columna in range(10):
        grid[fila].append(0) # Añade una celda

# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
# columnas empiezan en cero.)
grid[1][5] = 1

# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [512, 492]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la pantalla.
pygame.display.set_caption("Tetris")

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()


def dibujar(grid):
    # Dibujamos la retícula
    for fila in range(22):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = CYAN
            elif grid[fila][columna] == 2:
                color = MAGENTA
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])

#pieza = generarPieza(5)
fin = [False]
fondo = [22]
contador = [0]
# -------- Bucle Principal del Programa-----------

# Establecemos el fondo de pantalla.
pantalla.fill(NEGRO)
finJuego = False

cont = 0
while not hecho:
    for evento in pygame.event.get():   #para poder salir con X, quitarlo despues
        if evento.type == pygame.QUIT:  #para poder salir con X, quitarlo despues
            hecho = True                #para poder salir con X, quitarlo despues
    finCaida = False
    pieza = generarPieza(randint(1,7))
    print (pieza.coordenadas)
    pieza.coordenadas = reordenar_para_abajo(pieza.coordenadas)

    while not finCaida:
        for evento in pygame.event.get():   #para poder salir con X, quitarlo despues
            if evento.type == pygame.QUIT:  #para poder salir con X, quitarlo despues
                hecho = True                #para poder salir con X, quitarlo despues
                
        finCaida = caidaPieza(grid, 22, 10, pieza)
        dibujar(grid)
        reloj.tick(5)
        pygame.display.flip()
    pieza = None







    #if(cont == 44): finJuego = True




    # Limitamos a 20 fotogramas por segundo.


    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.


# Pórtate bien con el IDLE.
pygame.quit()
