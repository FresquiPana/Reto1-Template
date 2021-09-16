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
from DISClib.Algorithms.Sorting import quicksort as QSort
from DISClib.Algorithms.Sorting import shellsort as ShSort
from DISClib.Algorithms.Sorting import selectionsort as SSort
from DISClib.Algorithms.Sorting import mergesort as MSort
from DISClib.Algorithms.Sorting import insertionsort as ISort

sortingAlgorigthms = [ISort.sort, MSort.sort, SSort.sort, ShSort.sort, QSort.quicksort]

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
    print("6- req2")

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
    instanceCatalogo = catalogo
    instanceCatalogo["autores"]["elements"].sort(key=lambda elem: (int)(elem["BeginDate"]), reverse = True)
    resultado = []
    for i in instanceCatalogo["autores"]["elements"]:
        if (int)(i["BeginDate"])>(int)(annoFinal):
            continue
        if (int)(i["BeginDate"]) < (int)(annoInicial):
            break
        print(i["BeginDate"])
        resultado.append(i)
    resultado.reverse()
    return resultado

def req2(catalogo, annoInicial, annoFinal, sortFunction):
    """
    for i in range(lt.size(instanceCatalogo["obras"])):
        if lt.getElement(instanceCatalogo["obras"], i) == '':
            lt.deleteElement(instanceCatalogo["obras"], i)
    """
    instanceCatalogo = catalogo
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def sortingFunc(anno1, anno2):
        anno1use = anno1["DateAcquired"].split("-") if anno1["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)] #[2020, 10, 02]
        anno2use = anno2["DateAcquired"].split("-") if anno2["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]
        firstAnno = (int)(anno1use[0]) + ((months[(int)(anno1use[1])-1] + (int)(anno1use[2]))/365) #2020.344 
        secondAnno = (int)(anno2use[0]) + ((months[(int)(anno2use[1])-1] + (int)(anno2use[2]))/365)
        if((int)(firstAnno)>(int)(secondAnno)):
            return 1
        return 0
    sortingAlgorigthms[(int)(sortFunction)](lst = instanceCatalogo["obras"], cmpfunction = sortingFunc) # ShSort.sort(lst = instanceCatalogo["obras"], cmpfunction = sortingFunc)
    annoInicialUse = annoInicial.split("-") if annoInicial.split("-")!=[''] else ["0" for _ in range(3)] #[1920, 02, 20]
    firstAnno = (int)(annoInicialUse[0]) + ((months[(int)(annoInicialUse[1])-1] + (int)(annoInicialUse[2]))/365)#1920.216
    annoFinalUse = annoFinal.split("-") if annoFinal.split("-")!=[''] else ["0" for _ in range(3)] #[1985, 02, 20]
    lastAnno = (int)(annoFinalUse[0]) + ((months[(int)(annoFinalUse[1])-1] + (int)(annoFinalUse[2]))/365)#1985.216
    resultado = []
    for i in instanceCatalogo["obras"]["elements"]:
        dateAcquiredUse = i["DateAcquired"].split("-") if i["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]#[1920, 02, 20]
        dateNICE = (int)(dateAcquiredUse[0]) + ((months[(int)(dateAcquiredUse[1])-1] + (int)(dateAcquiredUse[2]))/365)#1920.216
        if (int)(dateNICE)>(int)(lastAnno):
            continue
        if (int)(dateNICE) < (int)(firstAnno):
            break
        resultado.append(i)
    resultado.reverse()
    for i in resultado:
        print(i["DateAcquired"])
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
        print(catalog["autores"]["elements"][4], "\n\n\n", catalog["obras"]["elements"][0]["DateAcquired"])
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
        resultado = req1(catalog, "1920", "1985")
        print(len(resultado)) #numero de artistas en el rango entregado
        print(resultado[0]) #
        print(resultado[1])
        print(resultado[2])
        print(resultado[-1])
        print(resultado[-2])
        print(resultado[-3])

    elif int(inputs[0]) == 6:
        req2(catalog, "1920-02-20", "1985-02-20", "3")

    else:
        sys.exit(0)
sys.exit(0)