# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import telepot

#Arreglo con las risas
risa = ["jajaja",'jaja','xD','lol','jeje','lel']

#Arreglo con los mensajes de animo
foo = ['Tu puedes Ing!', 
'Haz tu mejor esfuerzo','Si quieres triunfar, no te quedes mirando la escalera, empieza a subir, escalón por escalón, hasta que llegues arriba.','El que lucha siempre puede equivocarse, el que no, ya está equivocado.', 'Cuando pierdes, no te fijes en lo que has perdido, sino en lo que te queda por ganar.',
'Para triunfar en la vida, no es importante llegar el primero, para triunfar simplemente hay que llegar, levantándose cada vez que se cae en el camino.',
'No es verdaderamente grande aquel que nunca falla, si no el que nunca se da por vencido.',
' La VIDA no es fácil, pero si nos ESFORZAMOS y TRABAJAMOS DURO podemos conseguir TODO aquello que nos PROPONGAMOS','Lo único IMPOSIBLE en la vida, es aquello que no INTENTAS.']

#Método de la API que maneja los mensajes
def handle(msg):

#Los tipos de objetos que usaremos, se pueden ver en la página de la API de telegram
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    persona = msg['from']
    nombre = persona['first_name']
    
  #Se imprime en consola el comando que le llega al bot, no es necesario, así que quiere, borrelo
    print 'Got command: %s' % command
   
#Lista de comandos que el bot analiza, algunos regresan mensajes otros un sticker o una foto
#y se usan los objetos declarados arriba
    if command == '/start':
        bot.sendMessage(chat_id, str("Comando disponibles: /start /saludar /fecha /fotodeperfil /animo /amor /amorsticker /amorjapones /gracias /jaja /adios" ))
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
        bot.sendMessage(chat_id, str("Hasta mañana Ing " + nombre.encode('utf-8') + ", que pase buen día" ))
    elif command == '/animo':
	bot.sendMessage(chat_id, str(nombre.encode('utf-8') + ", " +random.choice(foo)))
    elif command == '/fecha':
        bot.sendMessage(chat_id, str("Ing " + nombre.encode('utf-8') + ", la fecha actual es: " + str(datetime.datetime.now())))
    elif command == '/fotodeperfil':
	bot.sendChatAction(chat_id, 'upload_photo')
        result = bot.sendPhoto(chat_id, open('/home/alejandro/Pictures/UFPS_Logo.png', 'rb'))
    elif command[:1]=='/' : bot.sendMessage(chat_id, str(nombre.encode('utf-8') + ", no tengo ese comando... (aún?)")) 	
    elif command == 'hehe' or command == '😆' or command == 'jeje' or command == 'lol' or command == 'jaja' or command =='ja' or command =='haha' or command =='hahaha' or command =='jajaja':
        bot.sendMessage(chat_id,random.choice(risa))
      
         
 # 		¡¡NO OLVIDE PONER EL TOKEN DEL BOT ABAJO!!
bot = telepot.Bot('EL TOKEN DEL BOT VA AQUÍ')
bot.notifyOnMessage(handle)
#esto se imprime cuando el bot empieza su ejecución
print 'Ando ejecutandome'

#No sé para que es, debe ser que permite que se mantenga en ejecución
while 1:
    time.sleep(10)
