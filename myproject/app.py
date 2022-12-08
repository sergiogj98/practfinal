from flask import Flask, render_template, request, redirect,request, escape
from search4web import search4letters, log_request
import time

app = Flask(__name__)
@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Bienvenido a la WebApp de Sergio Guillén',hora=time.strftime("%A %d de %B de %Y, %H:%M:%S"))

@app.route('/new',methods=['POST'])
def new_page() -> 'html':
    return render_template('new.html', the_title='Bienvenido Usuario Nuevo')

@app.route('/login',methods=['POST'])
def login_page() -> 'html':
    return render_template('login.html', the_title='Bienvenido, Identifíquese')

@app.route('/anonimous',methods=['POST'])
def anonimous_page() -> 'html':
    return render_template('anonimous.html', the_title='Bienvenido Usuario Anonimo')

@app.route('/identificado', methods=['POST'])
def identificado_page() -> 'html':
    usuario = request.form['usuario']
    return render_template('identificado.html', usuario=usuario)

@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results: '
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title=title,the_phrase=phrase, the_letters=letters, the_results=result)

@app.route('/viewlog')
def view_the_log() -> str:
    with open('search.log', 'r') as log:
        contents = log.read()
        return escape(contents)

if __name__  == '__main__':
    app.run()

