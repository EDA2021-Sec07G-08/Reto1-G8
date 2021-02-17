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
    print("1- Cargar información Videos-Large")
    print("2- Cargar informacion Videos-Small")
    print("3- Cargar informacion Category_ID")

catalog = None

def loadVideosLarge():

    return controller.loadVideosLarge("videos/videos-large.csv")

def loadVideosSmall():

    return controller.loadVideosSmall("videos/videos-small.csv")

def loadCategoryID():

    return controller.loadCategoryID("videos/category-id.csv")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        videos = loadVideosLarge()
        print("Total de videos cargados: "+ str(lt.size(videos)))
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        videos = loadVideosSmall()
        print("Total de videos cargados "+ str(lt.size(videos)))
    elif int(inputs[0] == 3):
        print("Cargando informacion de los archivos ....")
        videos = loadCategoryID()
        print("Total de categorias: "+ str(lt.size(videos)))
    else:
        sys.exit(0)
sys.exit(0)
