#1. Elabore un programa en Python que permita convertir de pesos a dólares, de
#pesos a euros, de euros a pesos, de pesos a yenes.
#1 yen = 26.30 pesos
#1 dólar = 3944 pesos
#1 euro = 4279 pesos
import os
import modules.ejercicio1.menuejer1 as mf
def eYen():
    if num >0:
        os.system('cls')
        num=int(input('Escribe un numero\n'))
        resul=(num/26.30)
        print(resul)        
    elif num<0:
         ('Solo numeros positivos')
    mf.menuejerfirst()
        
def eDolar():
    if num >0:
        os.system('cls')
        num=int(input('Escribe un numero\n'))
        resul=(num/3944)
        print(resul)
    elif num<0:
         ('Solo numeros positivos')
    mf.menuejerfirst()    

def eEuro():
    if num >0:
        os.system('cls')
        num=int(input('Escribe un numero\n'))
        resul=(num/4279)
        print(resul)
    elif num<0:
         ('Solo numeros positivos')
    mf.menuejerfirst()