# -*- coding: utf-8 *-*
import MySQLdb 

conn = MySQLdb.connect('localhost', 'ABarbara', 'root', '1dawabarbara')  # Abro la conexión 

def crearTabla(query):  # Le paso la cadena que realizará el create como parámetro.
	cursorCrear = conn.cursor()  #En un cursor (de la conexión) almaceno lo que quiero enviar a la base de datos.
	cursorCrear.execute(query)  #Ejecuto la orden
	cursorCrear.close() # Una vez utilizado, cierro mi cursor.

def insertarEmpleados():
	cursorInsertar= conn.cursor()
	for x in range(10):
		try:
			nombre = raw_input('Nombre: ')
			apellido = raw_input('Apellido: ')
			sueldoBase = comprobarSueldo(float(raw_input ('Sueldo base: ')))
			hijos = (int(raw_input('Número de hijos: ')))
			sueldoFinal = calcularImponible(sueldoBase, hijos)
			insert = (("INSERT INTO EMPLEADOS VALUES('%s', '%s', '%f', '%d', '%f')" ) % (nombre, apellido, sueldoBase, hijos, sueldoFinal))

			cursorInsertar.execute(insert) 

		except TypeError:
			print "Error, tipo de dato incorrecto"
		except Exception:
			print "Error"
	cursorInsertar.close()

def comprobarSueldo(sueldoBase):
	if sueldoBase<600:
		sueldoBase=600
	return sueldoBase

def calcularImponible(sueldo, hijos):
	if hijos>0:
		sueldoFinal= sueldo+((0.05*sueldo)*hijos)
	else:
		sueldoFinal= sueldo
	return sueldoFinal

def mostrarEmpleados():
	cursorMostrar= conn.cursor()
	cursorMostrar.execute('SELECT * FROM EMPLEADOS')
	fila= cursorMostrar.fetchone()
	while fila is not None:  # Mientras la fila no esté vacía
		print fila
		fila = cursorMostrar.fetchone()
	cursorMostrar.close()



cadenaCreate="CREATE TABLE EMPLEADOS (nombre varchar(100), apellido varchar(100), sueldo_base Decimal, hijos int, sueldo_final Decimal)"
crearTabla(cadenaCreate)
insertarEmpleados()
conn.commit() 
mostrarEmpleados()

conn.close()