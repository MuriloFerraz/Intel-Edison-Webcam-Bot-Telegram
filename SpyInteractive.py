#!/usr/bin/python

import sys
import time
import telepot
import cv2
import numpy
import mraa

TOKEN = 'sua chave'
bot = telepot.Bot(TOKEN)

capture = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
face_cascade = cv2.CascadeClassifier('/home/root/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/roothaarcascade_eye.xml')
