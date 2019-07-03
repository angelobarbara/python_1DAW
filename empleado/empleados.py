# -*- coding: utf-8 *-*
import MySQLdb 

conn = MySQLdb.connect('localhost', 'ABarbara', 'root', '1dawabarbara')  # Abro la conexión 

def crearTabla(query):  # Le paso la cadena que realizará el create como parámetro.
	cursor = conn.cursor()  #En un cursor (de la conexión) almaceno lo que quiero enviar a la base de datos.
	cursor.execute(query)  #Ejecuto la orden
	cursor.close() # Una vez utilizado, cierro mi cursor.

def insertarEmpleados():
	cursor= conn.cursor()
	for x in range(2):
		try:
			nombre = raw_input('Nombre: ')
			apellido = raw_input('Apellido: ')
			sueldoBase = comprobarSueldo(float(raw_input ('Sueldo base: ')))
			hijos = (int(raw_input('Número de hijos: ')))
			sueldoFinal = calcularImponible(sueldoBase, hijos)
			insert = (("INSERT INTO EMPLEADOS VALUES('%s', '%s', '%f', '%d', '%f')" ) % (nombre, apellido, sueldoBase, hijos, sueldoFinal))

			cursor.execute(insert) 

		except ValueError:
			print "Error, tipo de dato incorrecto"
		except Exception:
			print "Error"
	cursor.close()

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

crearTabla("CREATE TABLE EMPLEADOS (nombre varchar(100), apellido varchar(100), sueldo_base Decimal, hijos int, sueldo_final Decimal)")
insertarEmpleados()
conn.commit() 
conn.close()