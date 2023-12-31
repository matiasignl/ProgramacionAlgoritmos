# -*- coding: utf-8 -*-
"""Eva3_ProgramacionAlgoritmos_MatiasMarin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XKtG1jelC5IAbiyEL_sIbFJF4hNb0Y2w
"""

import numpy as np

#SE GENERA ARRAY CON LOTES, INGRESANDO "0" COMO LOTE DISPONIBLE Y "1" COMO LOTE VENDIDO
listado_lotes = np.array([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 1], [0, 1, 0, 0]])

#DECLARO LISTADO DE LOS DETALLES DE LOS LOTES, INGRESANDO NUMERO DE LOTE, TAMAÑO Y PRECOP
detalle_lotes = [
    {'Numero': 'Lote 1', 'Tamaño': '2500 m2', 'Precio': '$2.000.000'},
    {'Numero': 'Lote 2', 'Tamaño': '1500 m2', 'Precio': '$1.750.000'},
    {'Numero': 'Lote 3', 'Tamaño': '230 m2', 'Precio': '$250.000'},
    {'Numero': 'Lote 4', 'Tamaño': '700 m2', 'Precio': '$700.000'},
    {'Numero': 'Lote 5', 'Tamaño': '990 m2', 'Precio': '$900,000'},
]


# DECLARO LISTADO DE CLIENTES, COMO NULL, YA QUE SE RELLENA CONFORME SE SELECCIONEN LOTES
clientes = []

#DECLARO FUNCION PARA DESPLEGAR LISTADO DE LOTES, TRANSFORMO LOS VALORES A LOS INDICADOS EN EL DOCUMENTO, LOS 0(DISPONIBLES) PASAN A ESTAR VACIOS Y LOS 1(OCUPADOS) PASAN A SER "X"
def mostrar_lotes():
    print("Se Despliegan Lotes:")
    for fila in listado_lotes:
        for lote in fila:
            if lote == 0:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print("")

#DECLARO FUNCION PARA REALIZAR LA SELECCION DEL LOTE, SOLICITO LAS COORDENADAS DEL LOTE Y LA INFORMACION DEL CLIENTE QUE COMPRARA
def seleccionar_lote():
    print("Digite las Coordenadas del Lote (Fila, Columna):")
    try:
        fila = int(input("Ingrese Fila: "))
        columna = int(input("Ingrese Columna: "))
        if fila < 0 or fila >= listado_lotes.shape[0] or columna < 0 or columna >= listado_lotes.shape[1]:
            print("No Existe un Lote en las Coordenadas Ingresadas, Intente nuevamente")
            return
            #REALIZO VALIDACION DE DISPONIBILIDAD DEL LOTE SELECCIONADO, SI ESTA DISPONIBLE, PIDO DATOS DEL CLIENTE
        if listado_lotes[fila][columna] == 0:
            rut = input("Ingrese Rut: ")
            nombre = input("Ingrese Nombre: ")
            telefono = input("Ingrese Nro. de Teléfono: ")
            email = input("Ingrese Email: ")
            lote_seleccionado = {'Numero': detalle_lotes[fila]['Numero'], 'Cliente': {'Rut': rut, 'Nombre': nombre, 'Telefono': telefono, 'Email': email}}
            listado_lotes[fila][columna] = 1
            clientes.append(lote_seleccionado)
            print("El Lote Seleccionado Ha Sido Comprado")
        else:
            print("El Lote Seleccionado Ya Se Encuentra Vendido.")
    except ValueError:
        print("Las Coordenadas Ingresadas Son Inválidas, Ingreselas Nuevamente")

#DEFINO FUNCION PARA MOSTRAR EL DETALLE DE LOS LOTES VENDIDOS
def mostrar_detalle_lote():
    print("Ingrese las coordenadas del Lote Vendido:")
    try:
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        if fila < 0 or fila >= listado_lotes.shape[0] or columna < 0 or columna >= listado_lotes.shape[1]:
            print("Las Coordenadas Ingresadas Son Invalidas, Ingreselas Nuevamente")
            return
        if listado_lotes[fila][columna] == 1:
            detalles = detalle_lotes[fila]
            print("Detalles del lote Vendido:")
            print("Número: " + detalles['Numero'])
            print("Tamaño: " + detalles['Tamaño'])
            print("Precio: " + detalles['Precio'])
        else:
            print("El Lote Seleccionado No Se Ha Vendido")
    except ValueError:
        print("Las Coordenadas Ingresadas Son Invalidas")

#DEFINO FUNCION PARA REALIZAR DESPLIEGUE DE LA INFORMACION DE LOS CLIENTES QUE HAN COMPRADO UN LOTE, SI EXISTEN, MUESTRA LA INFO. SI NO, ENVIA UN MENSAJE INDICANDO QUE NO EXISTEN
def mostrar_clientes():
    if clientes:
        print("Listado De Clientes:")
        print("")
        for cliente in clientes:
            print("RUT Cliente: " + cliente['Cliente']['Rut'])
            print("Nombre: " + cliente['Cliente']['Nombre'])
            print("Teléfono: " + cliente['Cliente']['Telefono'])
            print("Email: " + cliente['Cliente']['Email'])
            print("Lote seleccionado: " + cliente['Numero'])
            print()
    else:
        print("Todavia No Hay Clientes Registrados :(")
        print("")

#DEFINO LA FUNCION PRINCIPAL DEL SISTEMA, EL MENU, SE DESPLEGARA SIEMPRE DESPUES DE TERMINAR UNA ACCION EN UNA DE LAS OPCIONES, LA UNICA OPCION QUE TERMINARA DEFINITIVAMENTE CON EL PROGRAMA ES LA DE SALIR
def menu():
    while True:
        print("----- Loteos DUOC -----")
        print("----- Menú -----")
        print("1. Ver Disponibilidad de Lotes")
        print("2. Seleccionar Un Lote")
        print("3. Ver Detalles del Lote Seleccionado")
        print("4. Ver Clientes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '5':
            print("Hasta Luego!")
            break
        elif opcion == '1':
            mostrar_lotes()
        elif opcion == '2':
            seleccionar_lote()
        elif opcion == '3':
            mostrar_detalle_lote()
        elif opcion == '4':
            mostrar_clientes()
        else:
            print("Opción Inválida, Ingrese Una Opción Valida")
print("")
menu()

