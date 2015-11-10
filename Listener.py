#!/usr/bin/python
import sys
import time
import telepot

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance2(msg)
	print (content_type, chat_id)
	mensagem = msg['text'].strip().lower()
	print mensagem

TOKEN = 'sua chave'
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Listening...'

while 1:
	time.sleep(10)
