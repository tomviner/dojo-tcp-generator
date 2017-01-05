import socket
from random import choice

import urbandictionary


urban_dic_objects = urbandictionary.random()

insult = 'You {}!'.format(urban_dic_objects[0].word)

praise = [
    'I like you',
    'You smell great',
    'Hope I see you again',
    'You are welcome',
]


TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024
MESSAGE = insult

print ('Sending: {0}'.format(MESSAGE))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
s.close()

print ('received data: {0}'.format(data.decode()))
