#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 28/11/2013
@note: Archivo de arranque para aplicacion de gestion de contactos con interfaz grafica.
@summary: Monitor de comunicaciones puerto serial.
@author: Sebastian Reyes Espinosa.
@organization: Técnica Humana S.A.S. 
@version: v0.5
@updated: 05/12/2013
'''

import serial
import time
import re

port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600, timeout=0, bytesize=8, stopbits=1)
ser.parity=serial.PARITY_NONE

time.sleep(2)
data = ser.readline()
data = data.replace("+", "")
data = data.replace('\r\n', "")
data = re.sub("\D", "", data)

if len(data) > 0:
    print data[-7:]
 
else:
    print 'Datos no recibidos'
ser.close()
