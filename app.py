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
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #2c3e50;
            }
            form {
                margin-bottom: 20px;
                background: #fff;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 0 5px rgba(0,0,0,0.1);
            }
            input, button {
                padding: 8px;
                margin: 5px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background-color: #3498db;
                color: Black;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #2980b9;
            }
        </style>
    </head>
    <body>
        <h1>Prototipo 3</h1>
        <form action="/contarVocales" method="get">
            <label>Introduce un texto para conocer el número de vocales:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        <form action="/palindromo" method="get">
            <label>Introduce un texto para saber si es palíndromo:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
         <form action="/capicuda" method="get">
            <label>Introduce un número para saber si es capicuda:</label><br>
            <input type="text" name="numero" placeholder="Introduce un número">
            <button type="submit">Resultado</button>
        </form>
        <form action="/contarPalabras" method="get">
            <label>Introduce un texto para contar la cantidad de palabras:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        </form>
        <form action="/palabraMasLarga" method="get">
            <label>Introduce un texto para saber cual es la palabra más larga y la cantidad de letras que tiene:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        <form action="/palabraMasLarga" method="get">
            <label>Introduce un texto para saber cual es la palabra más larga y la cantidad de letras que tiene:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        <form action="/contarTresLetras" method="get">
            <label>Introduce un texto para saber la cantidad de palabras de tres letras y el total de letras:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        <form action="/contarConsonantes" method="get">
            <label>Introduce un texto para saber el número de consonantes:</label><br>
            <input type="text" name="palabra" placeholder="Introduce un texto">
            <button type="submit">Resultado</button>
        </form>
        </form>
        <form action="/guardarResultado" method="get">
            <label>Introduce un texto para poder guardarlo:</label><br>
            <input type="text" name="guardar" placeholder="Introduce un texto">
            <button type="submit">Guardar</button>
        </form>
        <form action="/mostrarResultados" method="get">
        <input type="submit" value="Mostrar resultados guardados">
        </form>
        <form action="/borrarResultados" method="get">
        <input type="submit" value="Borrar todos los resultados">
        </form>
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
    opcion=request.args.get('guardar' '')
    return str(guardarResultado(opcion))
@app.route('/mostrarResultados')
def mostrar_resultados_ruta():
    return str(mostrarResultados())
@app.route('/borrarResultados')
def borrar_resultados_ruta():
    return str(borrarResultados())
if __name__ == '__main__':
    app.run(debug=True)