# -*- coding: utf-8 -*-
import sys
import telepot
from telepot.delegate import per_chat_id, create_open

import clases.correo


class botSistemas(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(botSistemas, self).__init__(seed_tuple, timeout)
        self._variable = 0
        self._mensaje = ""

    def on_chat_message(self, msg):
        self._mensaje = msg['text']
        nombre = (msg['from']['first_name']).encode('utf-8')
        if self._mensaje == "/correo":
            self.sender.sendMessage(nombre + ", ¿De qué profesor desea saber su correo?")
            self._variable = 1
            
             #En caso de que se haya pedido un correo anteriormente    
        elif self._variable == 1:
            self.sender.sendChatAction('typing')
            respuesta = clases.correo.correoB(self._mensaje) 
            self.sender.sendMessage("El correo del Ing " + respuesta)
            


TOKEN = ""

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(botSistemas, timeout=30)),
])
bot.notifyOnMessage(run_forever=True)
time.sleep(10)
