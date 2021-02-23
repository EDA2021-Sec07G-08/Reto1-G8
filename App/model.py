﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def AddVideosLargeLinked(videoslarge):

    videoslargelt = lt.newList(datastructure= 'SINGLE_LINKED',
                             filename= videoslarge)
    return videoslargelt

def AddVideosLargeArray(videoslarge):

    videoslargelt = lt.newList(datastructure ='ARRAY_LIST',
                            filename = videoslarge)
    return videoslargelt

def AddVideosSmall(videossmall):

    videossmalllt = lt.newList(datastructure= 'SINGLE_LINKED',
                                filename = videossmall)
    return videossmalllt

def addTagCategoryID(category_id):

    category_idlt = lt.newList(datastructure= 'SINGLE_LINKED',
                                filename = category_id)

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return(int(video1['views']) < int(video2['views']))

def sortsubList(catalog, size):

    sub_list = lt.subList(catalog, 0, size) 
    sub_list = sub_list.copy()
    return sub_list 

def ordenarCatalogo(catalog, tipo):

    if tipo == 'selection':
        start_time = time.process_time()
        sorted_list = ss.sort(catalog, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
    elif tipo == 'insertion':
        start_time = time.process_time()
        sorted_list = ins.sort(catalog, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
    elif tipo == 'shell':
        start_time = time.process_time()
        sorted_list = sa.sort(catalog, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
    
    return sorted_list, elapsed_time_mseg