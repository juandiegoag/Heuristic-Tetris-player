__author__ = 'rick9'
# -*- coding: utf-8 -*-
import random


# Clase encargada de los métodos del Algortitmo genético o Evolutivo

# Produce una gen de cuatro espacios, cada uno inicializado aleatoriamente
# Cada espacio representa una heurística
def producirGen():
    gen = []
    gen.append(random.uniform(6.0, 10.0))  # gen 0: recompensa líneas completadas
    gen.append(random.uniform(0.01, 0.06)) # gen 1: castiga agujeros
    gen.append(random.uniform(5.0, 9.0))   # gen 2: castiga altura
    gen.append(random.uniform(1.0, 4.0))   # gen 3: castiga bloqueos
    return gen


# Produce 4 genes, uno para cada individuo de la primera generación
def listaGenes():
    lista = []
    for x in range(4):
        lista.append(producirGen())
    return lista


# Se encarga de evaluar a la generación de genes pasada a partir de su desempeño en una partida de Tetris
# Se conservarán a los 2 genes con mejor desempeño para que sigan a la siguiente generación
def nuevaGeneracion(genes, puntajes):
   #Se seleccionan a los 2 genes con mejor puntuación
   indices = [i[0] for i in sorted(enumerate(puntajes), key=lambda x:x[1])]
   padre = genes[indices[2]]
   madre = genes[indices[3]]
   # A partir de los 2 sobrevivientes se llama a la función de apareo o CrossOver para producir descendencia
   hijo1 = crossOver1(padre, madre)
   hijo2 = crossOver2(padre, madre)
   # Ahora se sustituyen los genes viejos por una nueva generación "evolucionada"
   del genes[:]
   genes.append(padre)
   genes.append(madre)
   genes.append(hijo1)
   genes.append(hijo2)

   #Se reinician puntajes además
   for x in range(0,4):
       puntajes[x] = 0



# Función de apareamiento 1: Mezcla 2 genes, en este caso saca el promedio de sus pesos
def crossOver1(gen1, gen2):
    nuevoGen = list(map(lambda x,y: (x + y) / 2.0, gen1,gen2))
    return nuevoGen


# Función de apareamiento 2: Mezcla 2 genes, en este caso saca el promedio de sus pesos sumado a la resta entre 2
def crossOver2(gen1, gen2):
    nuevoGen = list(map(lambda x,y: ((x + y ) / 2.0) - ((x - y ) / -2.0), gen1,gen2))
    return nuevoGen