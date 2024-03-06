import os
from tabulate import tabulate
import modules.ejercicio1.exer1 as ef

def menuejerfirst():
    os.system('cls')
    titulo=[["MENU EJERCICIO 1"]]
    print(tabulate(titulo,tablefmt='double_grid'))
    opciones=[[ "1." "Convertir a yenes\n" "2.""Convertir a dolar\n""3.""Convertir a euro\n""4.""Salir\n"]]
    print(tabulate(opciones,tablefmt='double_grid'))
    opciones=input('>>')

    if opciones=="1":
        ef.eYen()
    elif opciones=="2":
        ef.eDolar()
    elif opciones=="3":
        ef.eEuro()
    elif opciones=="4":
        print('adios')
    else:
        menuejerfirst()
            
        