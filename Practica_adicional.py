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
    
# Programa Principal (PP)
if __name__=="__main__":
    while True:
        print('\n--- MENÚ PRINCIPAL ---')
        print('1. Contar vocales')
        print('2. Saber si es palindromo')
        print('3. Saber si es capicuda')
        print('4. Contar la cantidad de palabras')
        print('5. Buscar la palabra mas larga')
        print('6. Contar las palabras de tres letras')
        print('7. Contar consonantes')
        print('8. Guardar resultados')
        print('9. Mostrar antiguos resultados')
        print('10. Borrar resultados guardados')
        print('X. Para salir')
        opcion=input('Elige una opción: ').lower()

        if opcion=="x":
            print("Saliendo del programa...")
            break

        elif opcion=="1":
            palabra=input("Escribe una palabra: ")
            print(contarVocales(palabra))

        elif opcion=="2":
            palabra=input("Escribe una palabra: ")
            print(palindromo(palabra))

        elif opcion=="3":
            numero=input("Escribe un número: ")
            print(capicuda(numero))

        elif opcion=="4":
            texto=input("Escribe una frase: ")
            print(contarPalabras(texto))

        elif opcion=="5":
            texto=input("Escribe una frase: ")
            print(palabraMasLarga(texto))

        elif opcion=="6":
            texto=input("Escribe una frase: ")
            print(contarTresLetras(texto))

        elif opcion=="7":
            palabra=input("Escribe una palabra: ")
            print(contarConsonantes(palabra))

        elif opcion=="8":
            texto=input("Escribe el resultado que quieres guardar: ")
            print(guardarResultado(texto))

        elif opcion=="9":
            print(mostrarResultados())
        
        elif opcion=='10':
             print(borrarResultados())

        else:
            print("Opción inválida, intenta de nuevo.")