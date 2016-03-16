# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder pocner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot
import MySQLdb #para la conexión a la base de datos de datos mysql, recuerde tener instalado el paquete python-mysqldb
import conversorFechas



db = MySQLdb.connect(host="sandbox2.ufps.edu.co", # tu host, generalmente localhost
                     user="ufps_79", # nombre de usuario para la conexion a la base de datos
                      passwd="ufps_po", # contraseña para conectar a la base de datos
                      db="ufps_79", charset="utf8") # nombre de la base de datos, se define codificacion utf-8
db.names="uft8" #Se vuelve a definir codificación utf-8 para los nombres
cur = db.cursor()  #se inicializa el objetor cur el cual será nuestra manera de hacer consultas, más abajo se ve

#METODO PARA LA BUSQUEDA DE CORREOS
def correoPro(Cnombre):
	cur.execute('SELECT nombre, correo FROM profesor where nombre like "%'+ Cnombre + '%"')
	row = ""
	correo = ""
        for row in cur.fetchall():
            correo += str(row[1])
        return str(row[0].encode('utf-8')) + " es : " + str(row[1])


#METODO PARA LA BUSQUEDA DE ASESORIAS
def asesoriaPro(Anombre):
        cur.execute('SELECT nombre, horarioAseso FROM profesor where nombre like "%'+ Anombre + '%"')
	row = ""
	correo = ""
        for row in cur.fetchall():
            correo += str(row[1].encode('utf-8'))
        if(row[1].encode('utf-8')==""):
                return str(row[0].encode('utf-8')) + " es : No tiene horario de Asesoria"
        return str(row[0].encode('utf-8')) + " es : " + (row[1].encode('utf-8'))
    
    
def paginaPro(Pnombre):
        cur.execute('SELECT nombre, pagina FROM profesor where nombre like "%'+ Pnombre + '%"')
	row = ""
	correo = ""
        for row in cur.fetchall():
            correo += str(row[1].encode('utf-8'))
        if(row[1].encode('utf-8')==""):
                return str(row[0].encode('utf-8')) + " es : No tiene Página Web"
        return str(row[0].encode('utf-8')) + " es : " + (row[1].encode('utf-8'))