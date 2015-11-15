# SiluxTelegramBotPython
Bot de Telegram creado por el Semillero de Investigación en Linux y Desarrollo de Software Libre - SILUX
Tomado de los ejemplos de Telepot:

https://github.com/nickoala/telepot




## Pasos para Poderlo Ejecutar: 
1. Tener instalado Python 
2. Instalar the Python Package Manager:
```
    -sudo apt-get install python-pip

```
3. Instalar la librería de Telepot:
```
    -sudo pip install telepot 
 ```
4. y Finalmente Actualizar:
```
    -sudo pip install telepot --upgrade
```
Los pasos también están en la página de Telepot.

##Ejecución

Antes de ejecutar, hay que tener o adquirir un Token del Bot con ayuda del BotFather :

  -https://telegram.me/botfather
  
Si es necesario, se deben instalar las demás librerías de Python que permitirán diferentes funciones, en el caso de acceso a base de datos mysql, se debe instalar: 

    -sudo apt-get install python-mysqldb

Finalmente se coloca el bot Token en el código, en la línea:

    -bot = telepot.Bot('EL TOKEN DEL TU BOT')

Y se procede a ejecutar, en una terminal(dirigiendose antes a la locación):

    -python bot.py


Para Métodos y Funciones, las encontramos todos aquí:
https://github.com/nickoala/telepot
y 
https://github.com/nickoala/telepot/blob/master/REFERENCE.md

y la API de Telegram:

https://core.telegram.org/bots/api#available-types
