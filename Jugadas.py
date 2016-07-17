__author__ = 'rick9'
# -*- coding: utf-8 -*-
from operator import itemgetter
from Piezas import*
from Movimientos import*

# Modulo encargado de valorar el estado del tablero a partir de la irrupción de una pieza y así ver cual es la jugada a elegir

# IMPORTANTE: Función de evaluación de cada jugada. El puntaje no es el mismo que el puntaje de una partida, sino una valoracion
# de que tan conveniente es cierta jugada de acuerdo a los pesos de cada heurística
def valorarJugada(tablero, gen):
    puntaje = 0
    puntaje += gen[0] * filasLlenas(tablero) #Premio por líneas completadas
    puntaje -= gen[1] * agujeros(tablero)    #Castigo por agujeros
    puntaje -= gen[2] * sumaAlturas(tablero) #Castigo por alturas
    puntaje -= gen[3] * 0.5 #bloqueos(tablero)                    #Castigo por bloqueos (puede que no funcione)
    return puntaje


def evaluarJugadas(tablero, pieza, gen):
    copiaTablero = tablero[:]
    copiaPieza = pieza.coordenadas
    evaluacion = []

    #primero valoramos las jugadas hacia la izquierda
    #Y se simula como quedaría el tablero si se bajara la pieza en cualquier cantidad
    # de desplazamientos hacia la izquierda. Con esa simulación se valora la conveniencia de la jugada con valorarJugada
    movIzq = obtenerIzquierdo(copiaPieza)
    for i in range(1, movIzq + 1):
        copiaPieza = simulacionPiezaLados(copiaPieza, - i)
        movAbajo = obtenerFondo(copiaPieza,copiaTablero)
        copiaPieza = simulacionPiezaAbajo(copiaPieza, movAbajo)
        copiarPieza(copiaPieza,copiaTablero)
        valor = valorarJugada(copiaTablero,gen)
        descopiarPieza(copiaPieza,copiaTablero)
        evaluacion.append([ valor, -i ])
        #Se reestablecen los valores para la siguiente iteración
        copiaPieza = pieza.coordenadas
        copiaTablero = tablero[:]

    #ahora probamos jugadas a la derecha
    movDer = 9 - obtenerDerecho(copiaPieza)
    for i in range (1, movDer + 1):
        copiaPieza = simulacionPiezaLados(copiaPieza, i)
        movAbajo = obtenerFondo(copiaPieza,copiaTablero)
        copiaPieza = simulacionPiezaAbajo(copiaPieza, movAbajo)
        copiarPieza(copiaPieza,copiaTablero)
        valor = valorarJugada(copiaTablero, gen)
        descopiarPieza(copiaPieza,copiaTablero)
        evaluacion.append([ valor, i ])
        #Se reestablecen los valores para la siguiente iteración
        copiaPieza = pieza.coordenadas
        copiaTablero = tablero[:]

    #finalmente se evalúa la jugada sin realizar ningún desplazamiento
    movAbajo = obtenerFondo(copiaPieza,copiaTablero)
    copiaPieza = simulacionPiezaAbajo(copiaPieza, movAbajo)
    copiarPieza(copiaPieza,copiaTablero)
    valor = valorarJugada(copiaTablero, gen)
    descopiarPieza(copiaPieza,copiaTablero)
    evaluacion.append([ valor, 0 ])

    # Nótese que en evaluación se guarda la conveniencia de la jugada y el número de movimientos que hay que hacer para llevarla a cabo
    mejorJugada = max(evaluacion, key = itemgetter(0))
    return mejorJugada



# METODOS AUXILIARES PARA SIMULAR JUGADA------------------------------------
def obtenerIzquierdo(pieza):
    bloqueIzq = min(pieza, key = itemgetter(1))
    movIzq = bloqueIzq[1]
    return movIzq

def obtenerDerecho(pieza):
    bloqueDer = max(pieza, key = itemgetter(1))
    movDer = bloqueDer[1]
    return movDer

def simulacionPiezaLados(pieza, indice):
    piezaNueva = []
    for bloque in pieza:
        piezaNueva.append( [bloque[0], bloque[1] + indice] )
    return piezaNueva

def simulacionPiezaAbajo(pieza, indice):
    piezaNueva = []
    for bloque in pieza:
        piezaNueva.append( [bloque[0] + indice, bloque[1]] )
    return piezaNueva



def recorrerColumna(bloque, tablero):
    contador = 0
    for x in range(bloque[0] + 1, 22):
        if tablero[x][bloque[1]] == 0:
            contador += 1
        else:
            break
    return contador


def obtenerFondo(pieza, tablero):
    listaRecorridos = []
    for bloque in pieza:
        movAbajo = recorrerColumna(bloque,tablero)
        listaRecorridos.append(movAbajo)
    fondo = min(listaRecorridos)
    return fondo

def copiarPieza(pieza, tablero):
    for bloque in pieza:
        tablero[bloque[0]][bloque[1]] = 4

def descopiarPieza(pieza, tablero):
    for bloque in pieza:
        tablero[bloque[0]][bloque[1]] = 0


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

def filasLlenas(tablero):
    numLlenas = 0
    for x in range(0,21):
        if filaLlena(tablero[x]):
            numLlenas += 1
    return numLlenas





# FUNCIONES PARA MEDIR HEURÍSTICAS---------------------------------------
def agujeros(tablero):
    agujeros = 0
    for x in range(21,-1,-1):
        if filaVacia(tablero[x]):
            break
        else:
            for y in range(0,10):
                if tablero[x][y] == 0 and tablero[x - 1][y] != 0:
                    agujeros += 1
    return agujeros


def contarAltura(columna, tablero):
    reverso = 0
    for x in range(0, 22):
        if tablero[x][columna] == 0:
            reverso += 1
        else:
            break
    altura = 22 - reverso
    return altura


def sumaAlturas(tablero):
    suma = 0
    for x in range(0, 10):
        suma += contarAltura( x ,tablero)
    return suma

def bloqueos(tablero):
    bloqueos = 0
    for x in range(0,9):
        i = 21
        while tablero[i][x] != 0:
            if i > 1:
                 i -= 1
        while not filaVacia(tablero[i]):
           if i > 1:
                 i -= 1
           if tablero[i][x] != 0:
              bloqueos += 1
    return bloqueos



