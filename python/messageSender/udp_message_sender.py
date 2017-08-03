import socket


class udp_message_sender:
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message, address, port):
        self._socket.sendto(message, (address, port))
