from flask import Flask, request
from Practica_adicional import (
    contarVocales,
    palindromo,
    capicuda,
    contarPalabras,
    palabraMasLarga,
    contarTresLetras,
    contarConsonantes
)
app = Flask(__name__)
@app.route("/")
def inicio():
    return'''
    <h1>Prueba 1 (Valores fijos)</h1>
    <ul>
        <li><a href='/contarVocales'>Contar la cantidad de vocales de un texto (Hola mundo)</a></li>
        <li><a href='/palindromo'>Saber si una palabra es palindromo (Oso)</a></li>
        <li><a href='/capicuda'>Saber si un número es capicuda (101)</a></li>
        <li><a href='/contarPalabras'>Contar la cantidad de palabras de un texto (Hola mundo)</a></li>
        <li><a href='/palabraMasLarga'>Saber cual es la palabra más larga de un texto (Hola mundo)</a></li>
        <li><a href='/contarTresLetras'>Saber la cantidad de palabras de tres letras y el total de letras (Un oso)</a></li>
        <li><a href='/contarConsonantes'>Contar el número de consonantes (Hola mundo)</a></li>
    </ul>
    '''
@app.route('/contarVocales')
def contar_Vocales_Ruta():
    return str(contarVocales('Hola mundo'))
@app.route('/palindromo')
def palindromo_Ruta():
    return str(palindromo('Oso'))
@app.route('/capicuda')
def capicuda_Ruta():
    return str(capicuda('101'))
@app.route('/contarPalabras')
def contarPalabras_Ruta():
    return str(contarPalabras('Hola mundo'))
@app.route('/palabraMasLarga')
def palabraMasLarga_Ruta():
    return str(palabraMasLarga('Hola mundo'))
@app.route('/contarTresLetras')
def contarTresLetras_Ruta():
    return str(contarTresLetras('Un oso'))
@app.route('/contarConsonantes')
def contarConsonantes_Ruta():
    return str(contarConsonantes('Hola mundo'))
if __name__ == '__main__':
    app.run()