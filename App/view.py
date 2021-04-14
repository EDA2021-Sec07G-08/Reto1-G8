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
    print("1- Cargar información")
    print("2- Ordenar los videos por vistas")
    print("3- Cargar informacion Category_ID")
    print('4- Hacer una sublista')
    print("5 - Requerimiento 1")
    print('6 - Requerimiento 2')
    print("7 - Requerimiento 3")
    print("8 - Requerimiento 4")

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

def ordenarpaisycat(num, pais, category_id, catalog, categories):

    return controller.ordenarpaisycat(num, pais, category_id, catalog, categories)

def mastendenciacat(category_name, catalog, categories):

    return controller.mastendenciacat(category_name, catalog, categories)

def ordenarviewstag(tag, catalog, cantidad):

    return controller.ordenarviewstag(tag, catalog, cantidad)

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
            categories = loadCategoryID()
        elif funcion == 'Linked List':
            catalog = loadVideosLargeLinked()
            categories = loadCategoryID()
        else:
            print('El tipo de datastructure es incorrecto, intente de nuevo')
        print("Total de videos cargados: "+ str(lt.size(catalog)))
        lt = catalog['elements'][0]
        print(lt)
        print(categories)
    elif int(inputs[0]) == 2:
        tipo = input('Seleccione el tipo de ordenamiento (selection, insertion, shell, quick o merge) \n')
        size = input('Ingrese el tamaño de la muestra: \n')
        ans = controller.sortsubList(catalog, int(size))
        respuesta = ordenarCatalogo(ans, tipo)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(respuesta[1]))
    elif int(inputs[0]) == 3:
        print("Cargando informacion de los archivos ....")
        videos = loadCategoryID()
    elif int(inputs[0]) == 4:
        size = input('Ingrese el tamaño de la muestra: \n')
        result = controller.sortsubList(catalog, int(size))
        print(result)
    elif int(inputs[0]) == 5:
        num = input('Ingrese el numero de videos que se desean conocer: ')
        pais = input('Ingrese el nombre del pais: ')
        category_id = input('Ingrese el nombre de la categoria: ')
        ans = ordenarpaisycat(num, pais, category_id, catalog, categories)
        print(ans)
    elif int(inputs[0]) == 6:
        pais = input('Ingrese el nombre del pais: ')
        trending_video = controller.Requerimiento2(catalog,pais)
        print(trending_video[0]["title"]," " *10 ,trending_video[0]["channel_title"]," "*10,trending_video[0]["country"]," "*10,trending_video[1])
    elif int(inputs[0]) == 7:
        category_name = input('Ingrese el nombre de la categoria: ')
        ans = mastendenciacat(category_name, catalog, categories)
        print(ans)
    elif int(inputs[0]) == 8:
        tag = input('Ingrese el tag que desea buscar: ')
        cantidad = int(input('Ingrese el numero de videos que desea conocer: '))
        ans = ordenarviewstag(tag, catalog, cantidad)
        print(ans)
    else:
        sys.exit(0)
sys.exit(0)
