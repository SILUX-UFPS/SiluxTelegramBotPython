# -*- coding: utf-8 -*-
import sys
import telepot
from telepot.delegate import per_chat_id, create_open

import clases.profesor
import clases.informacion
import clases.controlador as controlador
import threading

def canal():
        threading.Timer(3600, canal).start()
        print "Enviando mensaje a canal"
      #  self.sender.sendMessage("@IngSistemasUFPSCanal" + controlador.enviarmensajecanal())
        bot.sendMessage('@IngSistemasUFPSCanal', controlador.enviarmensajecanal())

class botSistemas(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(botSistemas, self).__init__(seed_tuple, timeout)
        self._variable = 0
        self._mensaje = ""
        
  
        

    def on_chat_message(self, msg):
        #Tomamos el mensaje que llega
        self._mensaje = msg['text']
        #El nombre de la persona que envia el mensaje
        nombre = (msg['from']['first_name']).encode('utf-8')
        
        if self._mensaje == "/start":
            self.sender.sendMessage ("Hola! \nBienvenido al Bot de Ingeniería de Sistemas de la UFPS creado por el Semillero de Desarrollo de Software Libre y Linux. \n\nTengo disponibles los siguientes comandos: \n\n/correo Muestro correo de un profesor \n/asesoria Muestro los días de asesorias de un profesor \n/fecha Muestro la fecha de un evento (ej: primeros previos) \n/paginaWeb Muestro la página web de un profesor \n")
            
        
        elif self._mensaje == "/correo":
            self.sender.sendMessage(nombre + ", ¿De qué profesor desea saber su correo?")
            self._variable = 1
        
        elif self._mensaje == "/asesoria":
            self.sender.sendMessage(nombre + ", ¿De qué profesor desea saber su asesoria?")
            self._variable = 2
        
        elif self._mensaje == "/fecha":
            show_keyboard = {'keyboard': [['Primeros Previos'],['Segundos Previos'],['Exámenes Finales'],['Habilitaciones']]}
            self.sender.sendMessage(nombre + ", ¿de qué evento desea saber su fecha?",reply_markup=show_keyboard)
            self._variable = 3
        
        elif self._mensaje == "/paginaWeb":
            self.sender.sendMessage(nombre + ", ¿De qué profesor desea saber su Página Web?")
            self._variable = 4
        
        elif self._mensaje == "/informacion":
            show_keyboard = {'keyboard': [['Misión'],['Visión']]}
            self.sender.sendMessage("Escoge la información que quieres saber",reply_markup=show_keyboard)
            self._variable = 5
            
        elif self._mensaje == "/canal":
            print "Enviando mensaje a canal"
            bot.sendMessage('@IngSistemasUFPSCanal', controlador.enviarmensajecanal())


        
             #En caso de que se haya pedido un correo anteriormente    
        elif self._variable == 1:
            self.sender.sendChatAction('typing')
            try: 
                respuesta = clases.profesor.correoPro(self._mensaje)
            except Exception:
                self.sender.sendMessage("Escriba bien, no encontré nada")
            self.sender.sendMessage("El correo del Ing " + respuesta)
            self._variable = 0
        
        elif self._variable == 2:
            self.sender.sendChatAction('typing')
            respuesta = controlador.asesoriaProfesor(self._mensaje) 
            self.sender.sendMessage("La asesoria del Ing " + respuesta)
            self._variable = 0
               
        elif self._variable == 3:
            self.sender.sendChatAction('typing')
            try: 
                respuesta = clases.profesor.paginaPro(self._mensaje)
            except Exception:
                self.sender.sendMessage("Escriba bien, no encontré nada")
            self.sender.sendMessage("La Página Web del Ing " + respuesta)
            self._variable = 0
            
        elif self._variable == 4:
            self.sender.sendChatAction('typing')
            try: 
                respuesta = clases.profesor.paginaPro(self._mensaje)
            except Exception:
                self.sender.sendMessage("Escriba bien, no encontré nada")
            self.sender.sendMessage("La Página Web del Ing " + respuesta)
            self._variable = 0
            
        elif self._variable == 5:
            self.sender.sendChatAction('typing')
            respuesta = clases.informacion.info(self._mensaje)
            hide_keyboard = {'hide_keyboard': True}
            self.sender.sendMessage(respuesta,reply_markup=hide_keyboard)
            self._variable = 0
            
print "En ejecucion"
            
TOKEN = ""

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(botSistemas, timeout=30)),
])
canal()
bot.notifyOnMessage(run_forever=True)
time.sleep(10)

