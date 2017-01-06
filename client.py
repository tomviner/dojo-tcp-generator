import argparse
import socket
from random import choice
from time import sleep

import urbandictionary

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024
SEPARATOR = ('=========================')


def send_tcp_message(message):
    print ('\nSending: {0}'.format(message))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(message.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()

    print ('received data: {0}'.format(data.decode()))


def get_praise():
    return choice([
        'I like you',
        'You smell great',
        'Hope I see you again',
        'You are welcome',
    ])


def get_insult():
    urban_word = urbandictionary.random()[0]

    trump_insult = 'Trump says: You {}!'.format(urban_word.word)

    return urban_word, trump_insult


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--praise', action='store_true')

    args = parser.parse_args()

    praise = args.praise

    while 1:
        if praise:
            message = get_praise()
            definition_text = ''
        else:
            urban_word, message = get_insult()
            definition_text = (
                '\nDefinition of {}: {}\n'.format(
                    urban_word.word,
                    urban_word.definition
                )
            )

        print (SEPARATOR)
        send_tcp_message(message)

        if not praise:
            print (
                '\nDefinition of {}: {}\n'.format(
                    urban_word.word,
                    urban_word.definition
                )
            )
        print (SEPARATOR)
        sleep(4)
