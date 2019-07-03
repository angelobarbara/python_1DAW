# -*- coding: utf-8 *-*

import MySQLdb
from webbrowser import open

def ejecutarConsulta(query):
	conn = MySQLdb.connect('localhost', 'ABarbara', 'root', '1dawabarbara')  # Abro la conexión
	cursor= conn.cursor()
	cursor.execute(query)
	if query.upper().startswith('SELECT'):
		datos = cursor.fetchall()
	else:
		conn.commit()
		datos = None
	cursor.close()
	conn.close()
	return datos

def head(inicio='empleados'):
	return '<html><head><title>'+inicio+'</title></head><body>\n'

def parrafo(cadena):
	return '<p>'+cadena+'</p>\n'

def encabezado(cadena):
	return '<h1>'+cadena+'</h1>'

def tabla (filas):
	temp = '<table border="1">\n'

	for fila in filas:
		temp= temp + '<tr>'
		for celda in fila:
			temp= temp+ '<td>'+ str(celda)+ '<td>\n'
		temp= temp+'</tr>\n'
	return temp+ '</table>\n'

def final():
	return '</body> </html>'

f = open('empleados.html', 'w')
f.write(head())
f.write(encabezado('EMPLEADOS'))
f.write(parrafo('Lista de empleados ordenados por apellido'))
f.write(tabla(ejecutarConsulta('SELECT * FROM EMPLEADOS')))
f.write(final())
f.close()
