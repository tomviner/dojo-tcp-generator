import socket
import random


if __name__ == '__main__':

    HOST = '127.0.0.1'
    PORT = 8080

    def process_data(data):
        answers = [
            b"No You " + data,
            b"Tell that to your sister and/or brother!",
            b"You didn't!",
            b"That didn't even hurt my feelings",
        ]
        return random.choice(answers) + b'\n'

    while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while 1:
                    data = conn.recv(1024)
                    if not data:
                        break
                    response = process_data(data)
                    conn.sendall(response)
