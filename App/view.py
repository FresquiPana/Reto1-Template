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
    print("1- Cargar información en el catálogo")
    print("2- Numero de artistas")
    print('3- Numero de obras')
    print('4- Ultimos tres elementos (artistas & obras)')
    print("5- req1")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def req1(catalogo, annoInicial, annoFinal):
    catalogo["autores"]["elements"].sort(key=lambda elem: (int)(elem["BeginDate"]), reverse = True)
    resultado = []
    for i in catalogo["autores"]["elements"]:
        if (int)(i["BeginDate"])>annoFinal:
            continue
        if (int)(i["BeginDate"]) < annoInicial:
            break
        print(i["BeginDate"])
        resultado.append(i)
    resultado.reverse()
    return resultado

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Archivos cargados')
        print(catalog["autores"]["elements"][4], "\n\n\n", catalog["obras"]["elements"][0].keys())
        """
        catalog["autores"]["elements"].sort(key=lambda elem: (int)(elem["ConstituentID"]))
        catalog["obras"]["elements"].sort(key=lambda elem: (int)(elem["ObjectID"]))
        for i in catalog["autores"]["elements"]:
            print(i["ConstituentID"])
        print("\n\n")
        for i in catalog["obras"]["elements"]:
            print(i["ObjectID"])
        """
        


    elif int(inputs[0]) == 2:
        print("Cargando Artistas...")
        print('Artistas cargados: ' + str(lt.size(catalog['autores'])))


    elif int(inputs[0]) == 3:
        print("Cargando Obras...")
        print('Obras Cargadas: ' + str(lt.size(catalog['obras'])))
    

    elif int(inputs[0]) == 5:
        resultado = req1(catalog, 1920, 1985)
        print(len(resultado))
        print(resultado[0])
        print(resultado[1])
        print(resultado[2])
        print(resultado[-1])
        print(resultado[-2])
        print(resultado[-3])


    else:
        sys.exit(0)
sys.exit(0)