"""
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
import operator
from datetime import datetime, timedelta
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import mergesort as mgs
from DISClib.Algorithms.Sorting import quicksort as qks
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

def loadCategoryID(category_id):

    category_idlt = lt.newList(datastructure= 'ARRAY_LIST',
                                filename = category_id)

    lista = category_idlt['elements']

    categories_ids = [1,2,10,15,17,18,19,20,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44]

    j = 0

    dictnuevo = {}

    for i in range(len(lista)):

        diccionario = lista[i]   
        for clave, valor in diccionario.items():
            diccionario[clave] = valor.replace(str(categories_ids[j]) +'\t ', '')
            dictnuevo[categories_ids[j]] = diccionario[clave]
        j += 1

    return dictnuevo


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

def ordenarpaisycat(num, pais, category_name, catalog, categories):

    categories_ids = [1,2,10,15,17,18,19,20,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44]

    for i in range(len(categories_ids) - 1):
        key = categories_ids[i]
        if categories[key] == category_name:
            category_id = categories_ids[i]

    lista = catalog['elements']

    temp = lt.newList(datastructure='ARRAY_LIST')

    ans = []

    j = 1

    for i in range(0, len(lista)):
        lista_temporal = lista[i]
        if int(lista_temporal['category_id']) == int(category_id) and lista_temporal['country'] == pais:
            lt.addLast(temp, lista_temporal)

    sorted_list = mgs.sort(temp, cmpVideosByViewsMore)

    while j <= int(num):
        ans.append(lt.getElement(sorted_list, j))
        j += 1

    respuesta = []

    for i in range (len(ans)):
        diccionario = {}
        dict1 = ans[i]
        diccionario['trending_date'] = dict1['trending_date']
        diccionario['title'] = dict1['title']
        diccionario['channel_title'] = dict1['channel_title']
        diccionario['publish_time'] = dict1['publish_time']
        diccionario['views'] = dict1['views']
        diccionario['likes'] = dict1['likes']
        diccionario['dislikes'] = dict1['dislikes']
        respuesta.append(diccionario)

    return respuesta

def Requerimiento2(catalog,pais):
    listavideos = catalog
    dicres = {}
    for i in range(0,lt.size(listavideos)):
        video = lt.getElement(listavideos,i)
        if video["country"]== pais:
            if video["title"] in dicres:
                dicres[video["title"]] += 1
            else:
                dicres[video["title"]] = 1 
    videosort= sorted(dicres.items(),key=operator.itemgetter(1),reverse = True)
    trending_video = videosort[0][0]
    dias = videosort[0][1]
    for i in range (0,lt.size(listavideos)):
        video = lt.getElement(listavideos,i)
        if video["title"] == trending_video:
            return video,dias

def mastendenciacat(category_name, catalog, categories):

    categories_ids = [1,2,10,15,17,18,19,20,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44]

    for i in range(len(categories_ids) - 1):
        key = categories_ids[i]
        if categories[key] == category_name:
            category_id = categories_ids[i]

    lista_fin = []

    resp = {}

    lista = catalog['elements']

    for i in range(0, len(lista)):
        llave = lista[i]['title']
        if int(lista[i]['category_id']) == category_id:
            if llave not in resp:
                resp[llave] = 1
                lista_fin.append
            else:
                resp[llave] += 1

    list1 = [(title, trending_date) for title, trending_date in resp.items()]

    mayor = 0
    title = ''

    for i in range(len(list1)):
        if list1[i][1] > mayor:
            title = list1[i][0]
            mayor = list1[i][1]

    for i in range(0, len(lista)):
        title2 = lista[i]['title']
        if title == title2:
            ans = {}
            ans['title'] = title
            ans['channel_title'] = lista[i]['channel_title']
            ans['category_id'] = lista[i]['category_id']
            ans['dias'] = mayor

    return ans

def ordenarviewstag(tag, catalog, cantidad):

    lista = catalog['elements']

    for i in range(0, len(lista)):
        valorremplazo = lista[i]['tags']
        valorremplazo = valorremplazo.replace('"', '')
        valorremplazo = valorremplazo.split('|')
        lista[i]['tags'] = valorremplazo

    temp = lt.newList(datastructure='ARRAY_LIST')

    ans = []


    for i in range(0, len(lista)):
        lista_temporal = lista[i]
        for j in range(0, len(lista_temporal['tags'])):
            tags = lista_temporal['tags']
            if tags[j] == tag:
                lt.addLast(temp, lista_temporal)

    sorted_list = mgs.sort(temp, cmpVideosByLikes)

    j = 1
    while j <= (int(cantidad) + 1):
        ans.append(lt.getElement(sorted_list, j))
        j += 1

    respuesta = []

    for i in range (len(ans)):
        diccionario = {}
        dict1 = ans[i]
        diccionario['title'] = dict1['title']
        diccionario['channel_title'] = dict1['channel_title']
        diccionario['publish_time'] = dict1['publish_time']
        diccionario['views'] = dict1['views']
        diccionario['likes'] = dict1['likes']
        diccionario['dislikes'] = dict1['dislikes']
        respuesta.append(diccionario)

    return respuesta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViewsLess(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return(int(video1['views']) < int(video2['views']))

def cmpVideosByViewsMore(video1, video2):

    return(int(video1['views'])) > int(video2['views'])

def cmpVideosByLikes(video1, video2):

    return int(video1['likes']) > int(video2['likes'])

def cmpVideosByViewsLessorEqual(video1, video2):

    return(int(video1['views']) <= int(video2['views']))

def cmpVideosByTime(video1, video2):

    return(int(video1['trending_date']) > int(video2['trending_date']))

# Funciones de ordenamiento

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
    elif tipo == 'merge':
        start_time = time.process_time()
        sorted_list = mgs.sort(catalog, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif tipo == 'quick':
        start_time = time.process_time()
        sorted_list = qks.sort(catalog, cmpVideosByViewsLessorEqual)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000

    return sorted_list, elapsed_time_mseg