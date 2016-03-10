# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot
import MySQLdb #para la conexión a la base de datos de datos mysql, recuerde tener instalado el paquete python-mysqldb


db = MySQLdb.connect(host="",user="",passwd="",db="", charset="utf8") 
db.names="uft8" #Se vuelve a definir codificación utf-8 para los nombres
cur = db.cursor()  #se inicializa el objetor cur el cual será nuestra manera de hacer consultas, más abajo se ve

#Método para el manejo de las palabras claves del previo a buscar



def previo(clave):
    if clave== '':
	return 'No se ha recibido previo a buscar'

    cur.execute('SELECT nombre, correo FROM profesor where nombre like "%'+ command + '%"')
    for row in cur.fetchall(): 
        correo += str(row[1])
    
    return str("El correo del Ing " + str(row[0].encode('utf-8')) + " es : " + str(row[1])))
       


   	
