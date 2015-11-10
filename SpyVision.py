#!/usr/bin/python

import socket
import cv2
import numpy

TCP_IP = ''
TCP_PORT = 5052

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((TCP_IP, TCP_PORT))
serverSocket.listen(True)

capture = cv2.VideoCapture(0)
ret, img = capture.read()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
face_cascade = cv2.CascadeClassifier('/home/root/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/roothaarcascade_eye.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

def detect():
	ret, frame = capture.read()
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		result, imencode = cv2.imencode('.jpeg', img, encode_param)
			
print 'Intel Edison'
print 'Arquivos preparados'
print 'Principais funcoes prontas para serem executadas'
print 'Tudo pronto, aguardando conexoes...'

conn, add = serverSocket.accept()
while ret:
	detect()
	##result, imgencode = cv2.imencode('.jpg', img, encode_param)
	data = numpy.array(imencode)
	stringData = data.tostring()
	conn.send(str(len(stringData)).ljust(16));
	conn.send(stringData)
	
capture.release()
serverSocket.close()	
