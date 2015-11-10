#!/usr/bin/python
import telepot

TOKEN = 'sua chave'
bot = telepot.Bot(TOKEN)
mensagem = 'Esta eh uma mensagem enviada \n automaticamente por: \n Intel Edison'

bot.sendMessage(111111111, mensagem)
