"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información Videos-Large (Array_List o Linked_List)")
    print("2- Ordenar los videos por vistas")
    print("3- Cargar informacion Category_ID")
    print('4- Hacer una sublista')

catalog = None

def loadVideosLargeLinked():

    return controller.loadVideosLargeLinked("videos/videos-large.csv")

def loadVideosLargeArray():

    return controller.loadVideosLargeArray("videos/videos-large.csv")

def loadVideosSmall():

    return controller.loadVideosSmall("videos/videos-small.csv")

def loadCategoryID():

    return controller.loadCategoryID("videos/category-id.csv")

def ordenarCatalogo(catalog, tipo):

    return controller.ordenarCatalogo(catalog, tipo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        funcion = input(str('Array List o Linked List\n'))
        print("Cargando información de los archivos ....")
        if funcion == 'Array List':
            catalog = loadVideosLargeArray()
        elif funcion == 'Linked List':
            catalog = loadVideosLargeLinked()
        else:
            print('El tipo de datastructure es incorrecto, intente de nuevo')
        print("Total de videos cargados: "+ str(lt.size(catalog)))
    elif int(inputs[0]) == 2:
        tipo = input('Seleccione el tipo de ordenamiento (selection, insertion o shell) \n')
        size = input('Ingrese el tamaño de la muestra: \n')
        ans = controller.sortsubList(catalog, int(size))
        respuesta = ordenarCatalogo(ans, tipo)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(respuesta[1]))
    elif int(inputs[0]) == 3:
        print("Cargando informacion de los archivos ....")
        videos = loadCategoryID()
        print("Total de categorias: "+ str(lt.size(videos)))
    elif int(inputs[0]) == 4:
        size = input('Ingrese el tamaño de la muestra: \n')
        result = controller.sortsubList(catalog, int(size))
        print(result)
    else:
        sys.exit(0)
sys.exit(0)
