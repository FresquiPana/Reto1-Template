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

import ast
from prettytable import PrettyTable
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
    instanceCatalogo["autores"]["elements"].sort(key=lambda elem: (float)(elem["BeginDate"]), reverse = True)
    resultado = []
    for i in instanceCatalogo["autores"]["elements"]:
        if (float)(i["BeginDate"])>(float)(annoFinal):
            continue
        if (float)(i["BeginDate"]) < (float)(annoInicial):
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
        firstAnno = (float)(anno1use[0]) + ((months[(int)(anno1use[1])-1] + (float)(anno1use[2]))/365) #2020.344 
        secondAnno = (float)(anno2use[0]) + ((months[(int)(anno2use[1])-1] + (float)(anno2use[2]))/365)
        if((float)(firstAnno)>(float)(secondAnno)):
            return 1
        return 0
    sortingAlgorigthms[(int)(sortFunction)](lst = instanceCatalogo["obras"], cmpfunction = sortingFunc) # ShSort.sort(lst = instanceCatalogo["obras"], cmpfunction = sortingFunc)
    annoInicialUse = annoInicial.split("-") if annoInicial.split("-")!=[''] else ["0" for _ in range(3)] #[1920, 02, 20]
    firstAnno = (float)(annoInicialUse[0]) + ((months[(int)(annoInicialUse[1])-1] + (float)(annoInicialUse[2]))/365)#1920.216
    annoFinalUse = annoFinal.split("-") if annoFinal.split("-")!=[''] else ["0" for _ in range(3)] #[1985, 02, 20]
    lastAnno = (float)(annoFinalUse[0]) + ((months[(int)(annoFinalUse[1])-1] + (float)(annoFinalUse[2]))/365)#1985.216
    resultado = []
    for i in instanceCatalogo["obras"]["elements"]:
        dateAcquiredUse = i["DateAcquired"].split("-") if i["DateAcquired"].split("-")!=[''] else ["0" for _ in range(3)]#[1920, 02, 20]
        dateNICE = (float)(dateAcquiredUse[0]) + ((months[(int)(dateAcquiredUse[1])-1] + (float)(dateAcquiredUse[2]))/365)#1920.216
        if (float)(dateNICE)>(float)(lastAnno):
            continue
        if (float)(dateNICE) < (float)(firstAnno):
            break
        print(i["DateAcquired"], (float)(dateNICE), " > ",  (float)(firstAnno), (float)(dateNICE) < (float)(firstAnno), i["CreditLine"])
        resultado.append(i)
    resultado.reverse()
    #for i in resultado:
    #    print(i["DateAcquired"], dateNICE)
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
        print(catalog["autores"]["elements"][4], "\n\n\n", catalog["obras"]["elements"][0]["CreditLine"])
        obrasCompradas = [elem for elem in catalog["obras"]["elements"] if elem["CreditLine"] == "Purchase"]
        for i in obrasCompradas:
            print(i["CreditLine"])
        print(len(obrasCompradas), "\n\n\n")
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
        x = PrettyTable()
        x.field_names = resultado[0].keys()
        xd = [0,1,2,-3,-2,-1]
        for i in xd:
            x.add_row(resultado[i].values())
        print("\n\nNumero de artistas en el rango: \n", len(resultado)) #numero de artistas en el rango entregado
        print(x)
        
    elif int(inputs[0]) == 6:
        f= open(cf.data_dir + "/tableTry.txt","w+")
        resultado = req2(catalog, "1944-06-06", "1989-11-09", "1")
        x = PrettyTable()
        print([list(resultado[0].values())[3]])
        print(list(resultado[0].values())[:3] + list(resultado[0].values())[4:6] + [list(resultado[0].values())[3]] + list(resultado[0].values())[10:13]) #0(ObjectID),1(Title),2(ArtistsIDs),4(Medium),5(Dimensions),3(Date),10(DateAcquired),12(URL) [0,1,2,3,4,5,6,7,8,9,10,11,12]
        x.field_names = [*resultado[0]][:3] + [*resultado[0]][4:6] + [[*resultado[0]][3]] + [*resultado[0]][10:13]
        xd = [0,1,2,-3,-2,-1]
        for i in xd:
            artistasArray = []
            print([elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == "429"])
            for j in ast.literal_eval(list(resultado[i].values())[2]):
                print(j)
                print(next((elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == str(j)))["DisplayName"])
                artistasArray += [next((elem for elem in catalog["autores"]["elements"] if elem["ConstituentID"] == str(j)))["DisplayName"]]
            x.add_row(list(resultado[i].values())[:2] + [[dab for dab in artistasArray]] + list(resultado[i].values())[4:6] + [list(resultado[i].values())[3]] + list(resultado[i].values())[10:13])
        print("\n\nNumero de obras en el rango: \n", len(resultado)) #numero de obras en el rango entregado
        print("\nnumero de obras compradas: \n", len([elem for elem in resultado if ("Purchase" in elem["CreditLine"]) or ("purchase" in elem["CreditLine"])]))
        f.write(str(x))
        f.close()

    else:
        sys.exit(0)
sys.exit(0)