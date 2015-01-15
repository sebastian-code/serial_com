'''
Created on 24/12/2013
@author: rootmaster
'''

import socket

s = socket.socket()
s.bind(('localhost', 5000))
s.listen(1)

sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == 'K\r\n':
        break

    print 'Recibido en el servidor:', recibido
    #sc.send(recibido)

print 'adios'

sc.close()
s.close()
