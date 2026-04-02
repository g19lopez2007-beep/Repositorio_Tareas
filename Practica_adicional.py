'''
Este archivo usa importación circular. Para evitar problemas se necesita el otro archivo llamado Practica_adicional_funciones.py 
En este se contienen las funciones principales que se requieren para que sirva.
'''

from practica_adicional_funciones import (
    contarVocales, 
    palindromo, 
    capicuda, 
    contarPalabras, 
    palabraMasLarga, 
    contarTresLetras, 
    contarConsonantes, 
    guardarResultado, 
    mostrarResultados,
    borrarResultados
)

# Funciones Auxiliares
def contarVocalesAux(pNum):
    try:
        pNum=int(pNum)
        return 'Debe ingresar unicamente letras'
    except:
        return True

def palindromoAux(pNum):
    try:
        pNum=int(pNum)
        return 'Debe ingresar unicamente letras'
    except:
        return True

def capicudaAux(pNum):
    try:
        pNum=int(pNum)
        return True
    except:
        return 'Debe ingresar unicamente números'

def contarPalabrasAux(pNum):
    try:
        int(pNum)
        return 'Debe ingresar unicamente letras'
    except:
        return True

def palabraMasLargaAux(pNum):
    try:
        int(pNum)
        return 'Debe ingresar unicamente letras'
    except:
        return True

def contarTresLetrasAux(pNum):
    try:
        int(pNum)
        return 'Debe ingresar unicamente letras'
    except:
        i=0
        contador=0
        while i<len(pNum):
            if pNum[i]!=' ':
                contador+=1
            if pNum[i]==' ':
                contador=0
            if contador>=4:
                return "Las palabras solo pueden ser de 3 letras"
            i+=1
        if contador>=4:
            return "Las palabras solo pueden ser de 3 letras"
        return True

def contarConsonantesAux(pNum):
    try:
        int(pNum)
        return 'Debe de ingresar unicamente letras'
    except:
        return True