'''
Created on 24/12/2013

@author: rootmaster
'''
import socket

s = socket.socket()
s.connect(('localhost', 9999))

while True:
    mensaje = raw_input('> ')
    s.send(mensaje)
    if mensaje == 'salir':
        break

print 'adios'

s.close()

