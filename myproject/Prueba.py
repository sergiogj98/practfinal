dbconfig = { 'host': '127.0.0.1',
'user': 'root',
'password': 'SergioGJ123&',
'database': 'search_log', }

import mysql.connector
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """show tables""" #Sirve para ver las tablas que tenemos
cursor.execute(_SQL)
res = cursor.fetchall()

#_SQL = """describe log""" #Sirve para ver campos de tabla log
#cursor.execute(_SQL)
#res = cursor.fetchall()

#for row in res:
#   print(row)
#    for field in row:
#        print(field) #para acceder a cada uno de los campos

#_SQL = """select * from log""" #Todo lo de la tabla log
#cursor.execute(_SQL)
#res = cursor.fetchall()
#for row in res:
#    print(row)
#    print(row[1]) #Así hemos accedido al elemento de la tupla

#Así metemos elemento en tabla en un único comando   
#_SQL = """insert into log
#(phrase, letters, ip, browser_string, results)
#values
#('galaxia','aeiou', '127.0.0.1','Chrome',
#"{'a','i'}")"""
#cursor.execute(_SQL)

#Aqui introducimos en dos comandos
#_SQL = """insert into log
#(phrase, letters, ip, browser_string, results)
#values
#(%s, %s, %s, %s, %s)"""
#cursor.execute(_SQL, ('galaxia','bcdf', '127.0.0.1', 'Chrome', 'set()'))

#conn.commit()  #Hace efectivos  permanentes todos los cambios
#_SQL = """select * from log"""
#cursor.execute(_SQL)
#for row in cursor.fetchall():
#    print(row)


cursor.close() #Cierra cursor

conn.close() #Cierra conexion
