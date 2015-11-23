#! /usr/bin/python
import cv2
import time
import telepot

TOKEN = '111111111:AAAOaOaAaAAA1aataAq2qaa9XAAajAe35b8'
bot = telepot.Bot(TOKEN)

video_capture = cv2.VideoCapture(0)
#ret, img = video_capture.read()
#encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
face_cascade = cv2.CascadeClassifier('/home/root/haarcascade_frontalface_default.xml')

while True:
        ret, frame = video_capture.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        if len(faces) > 0:
                mensagem = "Encontrei {0} pessoas, verifique! \n Proximo aviso em 5 minutos." .format(.len(faces))
                bot.sendMessage(121111111, mensagem)
                time.sleep(300)

video_capture.release()
