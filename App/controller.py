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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos
def loadVideosLargeLinked(filename):

    videoslarge = cf.data_dir + filename
    return model.AddVideosLargeLinked(videoslarge)

def loadVideosLargeArray(filename):

    videoslarge = cf.data_dir + filename
    return model.AddVideosLargeArray(videoslarge)

def loadVideosSmall(filename):

    videossmall = cf.data_dir + filename
    return model.AddVideosSmall(videossmall)

def loadCategoryID(filename):

    category_id = cf.data_dir + filename
    return model.loadCategoryID(category_id)

# Funciones de ordenamiento

def sortsubList(catalog, size):

    return model.sortsubList(catalog, size)

def ordenarCatalogo(catalog, tipo):

    return model.ordenarCatalogo(catalog, tipo)

# Funciones de consulta sobre el catálogo

def ordenarpaisycat(num, pais, category_id, catalog, categories):

    return model.ordenarpaisycat(num, pais, category_id, catalog, categories)

def mastendenciacat(category_name, catalog, categories):

    return model.mastendenciacat(category_name, catalog, categories)

def ordenarviewstag(tag, catalog, cantidad):

    return model.ordenarviewstag(tag, catalog, cantidad)

def Requerimiento2(catalog,pais):
    return model.Requerimiento2(catalog,pais)