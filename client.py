import socket
from random import choice

import urbandictionary
import argparse
from time import sleep


def send_message(praise):
    urban_dic_objects = urbandictionary.random()

    urban_word = urban_dic_objects[0]

    insult = 'Trump says: You {}!'.format(urban_word.word)

    praises = [
        'I like you',
        'You smell great',
        'Hope I see you again',
        'You are welcome',
    ]

    TCP_IP = '127.0.0.1'
    TCP_PORT = 8080
    BUFFER_SIZE = 1024

    MESSAGE = insult
    if praise:
        MESSAGE = choice(praises)

    print ('=========================')
    print ('\nSending: {0}'.format(MESSAGE))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()

    print ('received data: {0}'.format(data.decode()))

    if not praise:
        print (
            '\nDefinition of {}: {}\n'.format(
                urban_word.word,
                urban_word.example
            )
        )
    print ('=========================')
    sleep(4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--praise', action='store_true')

    args = parser.parse_args()

    praise = args.praise
    while 1:
        send_message(praise)
