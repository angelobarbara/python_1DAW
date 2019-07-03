import MySQLdb


DB_HOST = '192.168.12.102'
DB_USER = 'ABarbara'
DB_PASS = 'root'
DB_NAME = '1dawabarbara'
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*datos)
# Conectar a la base de datos
cursor = conn.cursor()
# Crear un cursor
cursor.execute('''CREATE TABLE SUPERHEROES\
(superheroe varchar(20),identidad_secreta varchar(30),sexo varchar(10))''')

cursor.execute("INSERT INTO SUPERHEROES VALUES('Superman','Clark Kent','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Spiderman','Peter Parkder','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Boltie','Libby','Femenino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Capitan America','Steve Rogers','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Green Lantern','Hal Jordan','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('WonderWoman','Diana Prince','Femenino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Wolverine','Logan','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Mujer Invisible','Susan Storm','Femenino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Thor','Donald Blake','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Viuda Negra','Natasha Romanoff','Femenino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('IronMan','Tony Stark','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Batman','Bruce Waine','Masculino')")

cursor.execute("INSERT INTO SUPERHEROES VALUES ('Ruby Thursday','Thursday Rubinstein','Femenino')")

conn.commit()
cursor.close()
conn.close()

print 'Datos insertados'