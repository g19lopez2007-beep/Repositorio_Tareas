from flask import Flask, request
from Practica_adicional import (
    contarVocales,
    palindromo,
    capicuda,
    contarPalabras,
    palabraMasLarga,
    contarTresLetras,
    contarConsonantes,
    guardarResultado,
    borrarResultados,
    mostrarResultados
)
app = Flask(__name__)
@app.route("/")
def inicio():
    return'''
    <h1>Prototipo 2</h1>
    <ul>
        <strong>Introduce un texto para conocer el numero de vocales que tiene.
        <form action="/contarVocales" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para saber si es palindromo.
        <form action="/palindromo" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un número para saber si es capicuda.
        <form action="/capicuda" method="get">
        <input type="text" name="numero" placeholder="Introduce un número">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para contar la cantidad de palabras.
        <form action="/contarPalabras" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para saber cual es la palabra más larga y la cantidad de letras que tiene.
        <form action="/palabraMasLarga" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para saber la cantidad de palabras de tres letras y el total de letras.
        <form action="/contarTresLetras" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para saber el número de consonantes.
        <form action="/contarConsonantes" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Resultado">
        </form>
        Introduce un texto para poder guardarlo.
        <form action="/guardarResultado" method="get">
        <input type="text" name="palabra" placeholder="Introduce un texto">
        <input type="submit" value="Guardar">
        </form>
        <form action="/mostrarResultados" method="get">
        <input type="submit" value="Mostrar resultados guardados">
        </form>
        <form action="/borrarResultados" method="get">
        <input type="submit" value="Borrar todos los resultados">
        </form>
    </ul>
    '''
@app.route('/contarVocales')
def contar_Vocales_Ruta():
    opcion=request.args.get('palabra', '')
    return str(contarVocales(opcion))
@app.route('/palindromo')
def palindromo_Ruta():
    opcion=request.args.get('palabra' '')
    return str(palindromo(opcion))
@app.route('/capicuda')
def capicuda_Ruta():
    opcion=request.args.get('numero' '')
    return str(capicuda(opcion))
@app.route('/contarPalabras')
def contarPalabras_Ruta():
    opcion=request.args.get('palabra' '')
    return str(contarPalabras(opcion))
@app.route('/palabraMasLarga')
def palabraMasLarga_Ruta():
    opcion=request.args.get('palabra' '')
    return str(palabraMasLarga(opcion))
@app.route('/contarTresLetras')
def contarTresLetras_Ruta():
    opcion=request.args.get('palabra' '')
    return str(contarTresLetras(opcion))
@app.route('/contarConsonantes')
def contarConsonantes_Ruta():
    opcion=request.args.get('palabra' '')
    return str(contarConsonantes(opcion))
@app.route('/guardarResultado')
def guardar_Resultado():
    opcion=request.args.get('palabra' '')
    return str(guardarResultado(opcion))
@app.route('/mostrarResultados')
def mostrar_resultados_ruta():
    return str(mostrarResultados())
@app.route('/borrarResultados')
def borrar_resultados_ruta():
    return str(borrarResultados())
if __name__ == '__main__':
    app.run(debug=True)