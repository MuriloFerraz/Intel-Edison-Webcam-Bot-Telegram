#!/usr/bin/python

import sys
import time
import telepot
import cv2
import numpy
import mraa



# Listener - Metodo que rece e exibe no serial a mensagem
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance2(msg)
	print (content_type, chat_id)
	mensagem = msg['text'].strip().lower()
	print mensagem
	
	
	if mensagem == 'Hora':
		bot.sendMessage(chat_id, str(datetime.datetime.now()))
	
	else:
		bot.sendMessage(chat_id, 'Nao consegui entender o comando... \n Tente novamente...')


capture = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
face_cascade = cv2.CascadeClassifier('/home/root/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/roothaarcascade_eye.xml')

chat_id = 'chat_id aqui'
TOKEN = 'sua chave'
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Estou esperando comando ...'
while 1:
    time.sleep(10)
    
