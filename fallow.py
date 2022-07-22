# se debe descargar instalar la libreria instabot, debes ir a la terminal y escribir : pip install instabot

from instabot import Bot

mi_bot = Bot()
mi_bot.login(username='--1--', password='--2--')
mi_bot.follow_followers('--3--')

# --1-- colocas el nombre del instagram sin el @
#--2-- colocas la contraseña de tu cuenta
#--3--colocas el nombre de la persona famosa que tiene la audiencia objetivo , recuerda sin el @

# viendo unos blog de eeuu indican que no es recomendable usarlo mas de 4 a 5 veces o puedes bloquerte tu cuenta .