#pip3 install flask
#which pip 3 - caminho de instalação do pip3

from flask import Flask
from calculator import soma, sub, mult, div

app = Flask(__name__)

@app.route('/')
def index():
    h1 = '<h1>Calculadora Olist</h1>'
    ol = '''
            <ol>
                <li><a href="/soma">Somar</a></li>
                <li><a href="/sub">Subtrair</a></li>
                <li><a href="/mult">Multiplicar</a></li>
                <li><a href="/div">Dividir</a></li>
                
            </ol>
         '''
    return f'{h1} {ol}'

@app.route('/soma')
def somar():
    numero1 = 3.0
    numero2 = 5.0
    resultado = soma(numero1, numero2)

    h1 = '<h1>Calculadora </h1>'
    h3 = f'<h3>A soma de {numero1} + {numero2} = {resultado}.</h3'
    voltar = '<br/><br><br><br><a href="/">Voltar</a>'
    return f'{h1}{h3}{voltar}'

@app.route('/sub')
def subtrair():
    numero1 = 13.0
    numero2 = 5.0
    resultado = sub(numero1, numero2)

    h1 = '<h1>Calculadora </h1>'
    h3 = f'<h3>A subtração de {numero1} - {numero2} = {resultado}.</h3'
    voltar = '<br/><br><br><br><a href="/">Voltar</a>'
    return f'{h1}{h3}{voltar}'

@app.route('/div')
def dividir():
    numero1 = 15.0
    numero2 = 5.0
    resultado = div(numero1, numero2)

    h1 = '<h1>Calculadora </h1>'
    h3 = f'<h3>A divisão de {numero1} / {numero2} = {resultado}.</h3'
    voltar = '<br/><br><br><br><a href="/">Voltar</a>'
    return f'{h1}{h3}{voltar}'

@app.route('/mult')
def multiplicar():
    numero1 = 15.0
    numero2 = 5.0
    resultado = mult(numero1, numero2)

    h1 = '<h1>Calculadora </h1>'
    h3 = f'<h3>A multiplicação de {numero1} * {numero2} = {resultado}.</h3'
    voltar = '<br/><br><br><br><a href="/">Voltar</a>'
    return f'{h1}{h3}{voltar}'


app.run(debug=True) 
