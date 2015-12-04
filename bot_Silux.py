# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot
import MySQLdb #para la conexión a la base de datos de datos mysql, recuerde tener instalado el paquete python-mysqldb

#Lista con la risas
risa =["jajaja","jajajja","jajja","jjaja",'jaja','xD',u'\U0001f606','lol','jeje','lel','hehe','haha','hahaha','haa']
#Lista con los emoticones
emo = ["hola",":p",":3","e.e",":(",u"¬_¬",u"¬¬",u":/",u'\U0001f622']
#Lista con los saludos 
saludos = ["hello","hola",u"buenos días","buenass","buenos dias","buenas tardes","buenas noches"]
#Lista con las despedidas
despedidas = [u"adiós","hasta luego","nos vemos","chao",u"hasta mañana","sayonara"]

#Lista con los mensajes de animo
foo = ['Tu puedes Ing!', 
'Haz tu mejor esfuerzo','Si quieres triunfar, no te quedes mirando la escalera, empieza a subir, escalón por escalón, hasta que llegues arriba.','El que lucha siempre puede equivocarse, el que no, ya está equivocado.', 'Cuando pierdes, no te fijes en lo que has perdido, sino en lo que te queda por ganar.',
'Para triunfar en la vida, no es importante llegar el primero, para triunfar simplemente hay que llegar, levantándose cada vez que se cae en el camino.',
'No es verdaderamente grande aquel que nunca falla, si no el que nunca se da por vencido.',
' La VIDA no es fácil, pero si nos ESFORZAMOS y TRABAJAMOS DURO podemos conseguir TODO aquello que nos PROPONGAMOS','Lo único IMPOSIBLE en la vida, es aquello que no INTENTAS.']

#variables usadas para algunas validaciones
bolprevio = 0
fecha = ""
correo = ""
otra = ""
db = MySQLdb.connect(host="", # tu host, generalmente localhost
                     user="", # nombre de usuario para la conexion a la base de datos
                      passwd="", # contraseña para conectar a la base de datos
                      db="", charset="utf8") # nombre de la base de datos, se define codificacion utf-8
db.names="uft8" #Se vuelve a definir codificación utf-8 para los nombres
cur = db.cursor()  #se inicializa el objetor cur el cual será nuestra manera de hacer consultas, más abajo se ve

#Método de la API que maneja los mensajes
def handle(msg):

#Los tipos de objetos que usaremos, se pueden ver en la página de la API de telegram
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    persona = msg['from']
    nombre = persona['first_name']
	
    #ponemos en global algunas variables declaradas arriba para poder usarlas luego
    global otra 		
    print nombre + " "
   # print emo   
    global bolprevio
    global fecha
    global correo
    global saludos
    
  
#Se imprime en consola el comando que le llega al bot, no es necesario, así que quiere, borrelo
    print 'Dijo: %s' % command
   
#Lista de comandos que el bot analiza, algunos regresan mensajes otros un sticker o una foto
#y se usan los objetos declarados arriba
    if command == '/start':
        bot.sendMessage(chat_id, str("Comando disponibles: /start /saludar /fecha /fotodeperfil /animo /amor /amorsticker /amorjapones /gracias /jaja /adios" ))

    elif command.find("cierto bot?")>=0:
	bot.sendMessage(chat_id, str("Claro que sí"))
   	
   
    elif command.encode('utf-8') == "ボット愛してる":
	bot.sendMessage(chat_id, str("大好き❤️"))

    elif command == '/saludar':
        bot.sendMessage(chat_id, str("Hola " + nombre.encode('utf-8') +", soy el Bot del Semillero de investigación en Linux y desarrollo de Software libre, mucho Gusto"))	
    elif command == '/amorsticker':
        bot.sendSticker(chat_id, open('/home/alejandro/Pictures/heart.png'))
    elif command == '/amor':
        bot.sendMessage(chat_id, str("❤️"))
    elif command == '/amorjapones':
        bot.sendMessage(chat_id, str(nombre.encode('utf-8') + "大好き❤️"))
    elif command == '/gracias':
        bot.sendMessage(chat_id, str("De nada Ing " + nombre + " ;)" ))
    elif command == '/jaja':
        bot.sendMessage(chat_id, str("Jajajaja" ))
    elif command == '/adios':
        bot.sendMessage(chat_id, str("Hasta mañana Ing " + nombre.encode('utf-8') + ", que pase buena noche" ))
    #elif command.find("hasta mañana"):
     #   bot.sendMessage(chat_id, str("Hasta mañana Ing " + nombre.encode('utf-8') + ", que pase buena noche" ))
    elif command == '/animo':
	bot.sendMessage(chat_id, str(nombre.encode('utf-8') + ", " +random.choice(foo)))
    elif command == '/fecha':
        bot.sendMessage(chat_id, str("Ing " + nombre.encode('utf-8') + ", la fecha actual es: " + str(datetime.datetime.now())))
    elif command == '/fotodeperfil':
	bot.sendChatAction(chat_id, 'upload_photo')
        result = bot.sendPhoto(chat_id, open('/home/alejandro/Downloads/photo_2015-11-30_22-46-59.jpg', 'rb'))

	
#si recibimos el comando previo, declaramos la variable bolprevio para que en el siguiente mensaje se sepa que hacer
    elif command == '/previo':
        bolprevio = 1
        bot.sendMessage(chat_id, str("" + nombre.encode('utf-8') +", De qué previo desea saber información?"))
    
    elif command == '/correo':
        bolprevio = 2
        bot.sendMessage(chat_id, str("" + nombre.encode('utf-8') +", ¿De qué profesor desea saber su correo?"))

#método default para comandos que empiezan por /
    elif command[:1]=='/' : bot.sendMessage(chat_id, str(nombre.encode('utf-8') + ", no tengo ese comando... (aún?)"))


    elif command == '/matar':
        bolprevio = 1
        bot.sendMessage(chat_id, str("Estoy en ello..."))

 	
    #elif command in risa:  este método lo dejé asi porque ya no es necesario
    #bot.sendMessage(chat_id,random.choice(risa))

#en la comparación se hace intersección entre las dos listas, método de Python, si la intersección es true, continua
#luego para saber qué saludo envio comparamos otra vez las dos listas, esto nos regresa otra lista, y tomamos
#la posición cero
    elif any(y in command for y in saludos):
	#Holman sufrío mucho aquí, por culpa de esas comparaciones
	bot.sendMessage(chat_id,str([var for var in saludos if var in command][0].encode('utf-8').capitalize()+ " Ing. " + nombre.encode('utf-8')).title())

    elif any(x in command for x in risa):
	bot.sendMessage(chat_id, random.choice(risa))

    elif any(x in command for x in emo):
	bot.sendMessage(chat_id,str([var for var in emo if var in command][0].encode('utf-8')))
	
    elif command.find("d:")>=0:
	bot.sendMessage(chat_id, str("D:"))

    elif any(x in command for x in despedidas):
	bot.sendMessage(chat_id,str([var for var in despedidas if var in command][0].encode('utf-8').capitalize() + " Ing. " + nombre.encode('utf-8')))
	

    
#AQUI ESTÁN LAS VALIDACIONES CUANDO SE CAMBIAN LAS VARIABLES DE PREVIO y CORREO
    elif bolprevio == 1:
        bot.sendChatAction(chat_id, 'typing')#método que hace que el bot ponga "Escribiendo..."
            
        cur.execute('SELECT fecha, nombre FROM previos where nombre like "%'+ command + '%"') #comando SQL a ejecutar
#con el cur que declaramos más arriba
#tomamos todo lo que envía, depende de la consulta que hayas hecho
        for row in cur.fetchall(): 
            fecha += str(row[0])
#regresamos todo a normal
        bolprevio = 0
#enviamos la informacion, row es una lista con las columnas tomamos lo que aparezca en la 0 y 1, dependiendo
#de cómo hayamos hecho la consulta
        bot.sendMessage(chat_id,str("El día del previo de la materia " + str(row[1]) + " es :" + fecha ))
        fecha = ""          

    elif bolprevio == 2:
	bot.sendChatAction(chat_id, 'typing')
	cur.execute('SELECT nombre, correo FROM profesor where nombre like "%'+ command + '%"')
        for row in cur.fetchall(): 
            correo += str(row[1])
        bolprevio = 0
        bot.sendMessage(chat_id,str("El correo del Ing " + str(row[0].encode('utf-8')) + " es : " + str(row[1])))
        correo = ""

     
   	
         
#¡¡NO OLVIDE PONER EL TOKEN DEL BOT ABAJO!!

bot = telepot.Bot('')
bot.notifyOnMessage(handle)
#esto se imprime cuando el bot empieza su ejecución
print 'Ando ejecutandome'

#No sé para que es, debe ser que permite que se mantenga en ejecución
while 1:
    time.sleep(10)
