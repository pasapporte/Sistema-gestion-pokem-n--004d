import os
import msvcrt
import csv

#Cargar los pokemones del CSV
pokemones = ""
with open('pokemon_primera_generacion.csv', newline='', encoding='utf-8') as a:
    datos = csv.reader(a, delimiter=",")
    pokemones = list(datos)
#Creamos colección para el cinturon
cinturon = []
#Comenzamos sistema
while True:
    print("<<Press Any key>>")
    msvcrt.getch()
    os.system("cls")
    print("""\033[31m
    Sistema de Gestión Cinturón Pokémon
    ═══════════════════════════════════\033[0m
    1) Mostrar Pokemones
    2) Buscar Pokemon
    3) Agregar al cinturón
    4) Mostrar el cinturón
    5) Quitar del cinturón
    6) Generar reporte cinturon en CSV
    0) Salir      """)
    opcion = input("Seleccione : ")

    if opcion=="0":
        break
    elif opcion=="1":
        print("\033[33mListado de Pokemones\033[0m")
        for p in pokemones:
            print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")
    elif opcion=="2":
        print("\033[33mBuscar Pokemon\033[0m")
        nombre = input("Ingrese nombre para buscar: ").capitalize()
        centinela = False
        for p in pokemones:
            if p[1]==nombre:
                print(f"\033[32mENCONTRADO {p[0]}\t{p[1]}\t{p[2]}\tAltura: {p[3]}\tPeso: {p[4]}\033[0m")
                centinela = True
                break
        if not centinela:
            print("\033[31mPokemon NO encontrado\033[0m")
    elif opcion=="3":
        print("\033[33mAgregar Cinturón\033[0m")
        if len(cinturon)<6:
            nombre = input("Ingrese nombre para buscar: ").capitalize()
            centinela = False
            for p in pokemones:
                if p[1]==nombre:
                    print(f"\033[32mENCONTRADO {p[0]}\t{p[1]}\t{p[2]}\tAltura: {p[3]}\tPeso: {p[4]}\033[0m")
                    #Validando que el pokémon no se repita
                    repetido = False
                    for pok in cinturon:
                        if pok[1]==nombre:
                            repetido = True
                    if not repetido:
                        cinturon.append(p)
                        print("\033[32mPokemon Registrado\033[0m")
                    else:
                        print("\033[31mPokemon Repetido\033[0m")
                    #####################################
                    centinela = True
                    break #Romper la busqueda si ya se encontró
            if not centinela:
                print("\033[31mPokemon NO encontrado\033[0m")
        else:
            print("\033[31mCinturón sin espacio disponible\033[0m")
    elif opcion=="4":
        print("\033[33mMostrar Cinturón\033[0m")
        if len(cinturon)>0:
            for i in range(len(cinturon)):
                print(f"{i+1} {cinturon[i][1]} {cinturon[i][2]}")
        else:
            print("\033[31mCinturón Vacío\033[0m")
    elif opcion=="5":
        print("\033[33mQuitar del Cinturón\033[0m")
        nombre = input("Ingrese nombre para quitar: ").capitalize()
        centinela = False
        for p in cinturon:
            if p[1] == nombre:
                cinturon.remove(p)
                print("\033[32mPokemon quitado\033[0m")
                centinela =True
                break
        if not centinela:
            print("\033[31mPokémon no encontrado\033[0m")
    elif opcion=="6":
        if len(cinturon)>0:
            with open('reporte_cinturon.csv','w',newline='',encoding='utf-8') as a:
                escritura = csv.writer(a, delimiter=',')
                escritura.writerows(cinturon)
            print("\033[32mReporte Generado\033[0m")
        else:
            print("\033[31mNo hay pokemones en el cinturón\033[0m")
    else:
        print("\033[31mOpción no valida\033[0m")

