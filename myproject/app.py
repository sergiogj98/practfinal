from flask import Flask, render_template, request, redirect,request, escape
from search4web import search4letters_upgrade, log_request
import time
from datetime import datetime
from DBcm import UseDatabase, CredentialsError, ConnectionError, SQLError

dbconfig = { 'host': '127.0.0.1',
'user': 'root',
'password': 'SergioGJ123&',
'database': 'search_log', }

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

@app.route('/login_nw',methods=['POST'])
def login_nw_page() -> 'html':
    return render_template('login.html', the_title='Bienvenido, identifíquese por favor')

@app.route('/login',methods=['POST'])
def login_page() -> 'html':
    usuario = request.form['usuario']
    password = request.form['password']
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select username from user"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        found = 0
        for i in range(len(res)):
            print(res[i][0])
            if (usuario==res[i][0]): # EL USUARIO ESTA EN LA BASE DE DATOS, POR LO QUE NO PUEDE CREAR EL MISMO USUARIO
                found =1
    if found==1:
        return render_template('new.html',the_title='Lo sentimos, el usuario introducido ya se encuentra en la base de datos. Por favor, introduzca un nuevo usuario')
    else:
        with UseDatabase(dbconfig) as cursor:
            _SQL = """insert into user (username,password) values (%s,%s)"""
            cursor.execute(_SQL, (usuario,password))
            res = cursor.fetchall()
        return render_template('login2.html', the_title='Usuario creado satisfactoriamente. Por favor, identifíquese')

@app.route('/anonimous',methods=['POST'])
def anonimous_page() -> 'html':
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select * from visits"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        if(res==[]): #TODAVIA NO HA HABIDO NINGUNA VISITA
            with UseDatabase(dbconfig) as cursor:
                _SQL = """insert into visits (user,n_visits) values ('anonymous','1')"""
                cursor.execute(_SQL)
                res = cursor.fetchall()
        else:
            with UseDatabase(dbconfig) as cursor:
                _SQL = """select n_visits from visits where user='anonymous'"""
                cursor.execute(_SQL)
                res = cursor.fetchall()

            count = res[0][0]
            count += 1

            with UseDatabase(dbconfig) as cursor:
                _SQL = """update visits SET n_visits = %s where user = 'anonymous'"""
                cursor.execute(_SQL, (count,))
                res = cursor.fetchall()

                _SQL = """insert into log (ts,phrase,letters,ip,browser_string,results,user) values ('2017-07-23 00:00:00','','','','','','anonymous')"""
                cursor.execute(_SQL)
                res = cursor.fetchall()

    return render_template('anonimous.html', the_title='Bienvenido Usuario',the_user='anonymous')

@app.route('/identificado', methods=['POST'])
def identificado_page() -> 'html':
    usuario = request.form['usuario']
    password = request.form['password']
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select id from user where username = %s and password = %s"""
        cursor.execute(_SQL, (usuario,password))
        res = cursor.fetchall()
        if res!=[]: #HA ENCONTRADO AL USUARIO
            with UseDatabase(dbconfig) as cursor:
                _SQL = """select n_visits from visits where user = %s"""
                cursor.execute(_SQL, (usuario,))
                res = cursor.fetchall()
                if (res == []):  # TODAVIA ESE USUARIO AUN NO HA VISITADO LA WEB
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """insert into visits (user,n_visits) values (%s,'1')"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()
                else:
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """select n_visits from visits where user=%s"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()

                    count = res[0][0]
                    count += 1

                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """update visits SET n_visits = %s where user = %s"""
                        cursor.execute(_SQL, (count,usuario))
                        res = cursor.fetchall()

                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """insert into log (ts,phrase,letters,ip,browser_string,results,user) values ('2017-07-23 00:00:00','','','','','',%s)"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """select max(ts) from log where user=%s"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()
                        fecha=res[0][0]
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """select phrase from log where ts=%s"""
                        cursor.execute(_SQL, (fecha,))
                        res = cursor.fetchall()
                        frase=res[0][0]

            return render_template('identificado.html', usuario=usuario, the_visit=count,the_date=fecha, the_phrase=frase)
        else:
            return render_template('login.html',the_title='Lo sentimos, el usuario y/o contraseñas introducidas no coinciden. Por favor, pruebe a introducirlas de nuevo.')

@app.route('/identificado2', methods=['POST'])
def identificado2_page() -> 'html':
    usuario = request.form['usuario']
    password = request.form['password']
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select id from user where username = %s and password = %s"""
        cursor.execute(_SQL, (usuario,password))
        res = cursor.fetchall()
        if res!=[]: #HA ENCONTRADO AL USUARIO
            with UseDatabase(dbconfig) as cursor:
                _SQL = """select n_visits from visits where user = %s"""
                cursor.execute(_SQL, (usuario,))
                res = cursor.fetchall()
                if (res == []):  # TODAVIA ESE USUARIO AUN NO HA VISITADO LA WEB
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """insert into visits (user,n_visits) values (%s,'1')"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()
                else:
                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """select n_visits from visits where user=%s"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()

                    count = res[0][0]
                    count += 1

                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """update visits SET n_visits = %s where user = %s"""
                        cursor.execute(_SQL, (count,usuario))
                        res = cursor.fetchall()

                    with UseDatabase(dbconfig) as cursor:
                        _SQL = """insert into log (ts,phrase,letters,ip,browser_string,results,user) values ('2017-07-23 00:00:00','','','','','',%s)"""
                        cursor.execute(_SQL, (usuario,))
                        res = cursor.fetchall()

            return render_template('identificado2.html', usuario=usuario)
        else:
            return render_template('login.html',the_title='Lo sentimos, el usuario y/o contraseñas introducidas no coinciden. Por favor, pruebe a introducirlas de nuevo.')

@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Aquí están tus resultados'
    result, statis = search4letters_upgrade(phrase, letters)
    result = str(result)
    log_request(request, result)

    with UseDatabase(dbconfig) as cursor:
        _SQL = """select max(id) from log"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        max_id = res[0][0]

        _SQL = """update log set ts=%s,phrase=%s,letters=%s,ip=%s,browser_string=%s,results=%s where id=%s"""
        cursor.execute(_SQL, (str(datetime.now()), phrase, letters, str(request.remote_addr), str(request.user_agent), result, max_id))
        res = cursor.fetchall()
    if len(statis)==3:
        return render_template('results.html',the_title=title,the_phrase=phrase, the_letters=letters, the_results=result,statistics=statis)
    else:
        return render_template('results1.html',the_title=title,the_phrase=phrase, the_letters=letters, the_results=result)

@app.route('/contact')
def contact_page() -> 'html':
    return render_template('contact.html')

@app.route('/viewlog')
def view_the_log() -> str:
    with open('search.log', 'r') as log:
        contents = log.read()
        return escape(contents)

@app.route('/statistics',methods=['POST'])
def statistics_page() -> 'html':
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select n_visits from visits"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        count_visit=0
        for i in range(len(res)):
            count_visit+=res[i][0]

        _SQL = """select * from user"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        count_user = len(res)

        _SQL = """select user from visits where n_visits = (select max(n_visits) from visits)"""
        cursor.execute(_SQL)
        res = cursor.fetchall()
        top=res[0][0]
        print(top)

    return render_template('statistics.html', the_title='ESTADISTICAS',the_user=count_user, the_visit=count_visit, the_top=top)

if __name__  == '__main__':
    app.run()

