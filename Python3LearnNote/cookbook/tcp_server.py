from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

    # >> > from socket import socket, AF_INET, SOCK_STREAM
    # >> > s = socket(AF_INET, SOCK_STREAM)
    # >> > s.connect(('localhost', 20000))
    # >> > s.send(b'Hello')
    # 5
    # >> > s.recv(8192)
    # b'Hello'
    # >> >