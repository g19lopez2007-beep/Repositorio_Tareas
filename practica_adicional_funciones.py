'''
Este archivo usa importación circular. Para evitar problemas se necesita el otro archivo llamado Practica_adicional.py 
En este se contienen las funciones auxiliares que se requieren para que sirva y,
aparte, tiene los print para poder ver los resultados.
'''

def contarVocales(pNum):
    from Practica_adicional import contarVocalesAux
    if not contarVocalesAux(pNum):
        return(contarVocalesAux(pNum))
    contador=0
    vocales="aeiou"
    i=0
    while i<len(pNum):
        if pNum[i].lower() in vocales:
            contador+=1
        i+=1
    return f'El numero de vocales que tiene es: {contador}'

def palindromo(pNum):
    from Practica_adicional import palindromoAux
    if palindromoAux(pNum)!=True:
        return(palindromoAux(pNum))
    i=len(pNum)-1
    u=0
    while u<i:
        if pNum[i].lower()!=pNum[u].lower():
            return 'No es palindromo'
        i-=1
        u+=1
    return 'Es palindromo'

def capicuda(pNum):
    from Practica_adicional import capicudaAux
    if capicudaAux(pNum)!=True:
        return(capicudaAux(pNum))
    pNum=str(pNum)
    i= len(pNum)-1
    u= 0
    while u<i:
        if pNum[i]!=pNum[u]:
            return 'No es capicuda'
        i-=1
        u+=1
    return 'Es capicuda'

def contarPalabras(pNum):
    from Practica_adicional import contarPalabrasAux
    if contarPalabrasAux(pNum)!=True:
        return(contarPalabrasAux(pNum))
    pNum=str(pNum)
    if len(pNum)==0:
        return 'Debe de ingresa minimo una palabra'
    i=0
    contador=1
    while i<len(pNum):
        if pNum[i]==" ":
            contador+=1
        i+=1
    return f'La cantidad de palabras es: {contador}'

def palabraMasLarga(pNum):
    from Practica_adicional import palabraMasLargaAux
    if palabraMasLargaAux(pNum)!=True:
        return(palabraMasLargaAux(pNum))
    if len(pNum)==0:
        return "Debe de ingre minimo una palabra"
    i=0
    valor=0
    mayor=0
    palabraAux=''
    palabra=''
    while i<len(pNum):
        if pNum[i]!=' ':
            valor+=1
            palabraAux=palabraAux+pNum[i]
        elif pNum[i]==' ':
            if valor>mayor:
                mayor=valor
                palabra=palabraAux
            valor=0
            palabraAux=''
        i+=1
    if valor > mayor:
        mayor = valor
        palabra = palabraAux
    return f'La palabra más larga es: [{palabra}] y contiene: {mayor} letras'

def contarTresLetras(pNum):
    from Practica_adicional import contarTresLetrasAux
    if contarTresLetrasAux(pNum)!=True:
        return(contarTresLetrasAux(pNum))
    pNum=str(pNum)
    i=0
    palabra=''
    letra=0
    separacion=1
    while i<len(pNum):
        if pNum[i]!=' ':
            palabra=palabra+pNum[i]
            letra+=1
        if pNum[i]==' ':
            palabra=palabra+", "
            separacion+=1
        i+=1
    return f'La palabra es: {palabra} y contine esta cantidad de palabras: {separacion} y un total de letras de: {letra}'

def contarConsonantes(pNum):
    from Practica_adicional import contarConsonantesAux
    if contarConsonantesAux(pNum)!=True:
        return(contarConsonantesAux(pNum))
    pNum=str(pNum)
    i=0
    consonantes='qwrtypsdfghkjlzxcvbnmñ'
    contador=0
    while i<len(pNum):
        if pNum[i].lower() in consonantes:
            contador+=1
        i+=1
    return f'El numero de consonantes son: {contador}'