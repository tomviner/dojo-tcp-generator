import socket


if __name__ == '__main__':

    HOST = '127.0.0.1'
    PORT = 8080

    def process_data(data):
        return data[::-1]

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
