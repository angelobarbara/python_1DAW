# -*- coding: utf-8 *-*
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'ABarbara'
DB_PASS = 'root'
DB_NAME = '1dawabarbara'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
    cursor = conn.cursor()          # Crear un cursor
    cursor.execute(query)           # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()    # Traer los resultados de un select
    else:
        conn.commit()      # Hacer efectiva la escritura de datos
        data = None
    cursor.close()         # Cerrar el cursor
    conn.close()           # Cerrar la conexión
    return data

def inicio(string):
      return '<html><head><title>' + string + '</title></head> <body>\n'
def parrafo(string):
    return '<p>' + string + '</p>\n'

def encabezado(string):
    return '<h1>'+ string + '</h1>'
def tabla(array):
        temp =  '<table border="1">\n'

        for linea in array:
            temp = temp + '<tr>'
            for celda in linea:
                temp = temp + '<td>' + str(celda) + '</td>\n'
            temp = temp + '</tr>\n'
        return temp + '</table>\n'

def final():
    return '</body> </html>'
f = open('superheroes.html','w')
f.write(inicio('Tabla Superheroes'))
f.write(encabezado('Tabla de Superheroes'))
f.write(parrafo('Superheroes ordenados por nombre de superheroe'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY superheroe')))
f.write(parrafo('Superheroes ordenados por nombre de identidad secreta'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY identidad_secreta')))
f.write(final())
f.close()