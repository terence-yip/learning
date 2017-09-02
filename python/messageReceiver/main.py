#!/usr/bin/python
import socket
import argparse


def main():
    parser = argparse.ArgumentParser(description='Listen for messages')
    parser.add_argument('-a', '--address', type=str, default='127.0.0.1',
                        help='Host address')
    parser.add_argument('-p', '--port', type=int, default='50000',
                        help='Port')
    args = parser.parse_args()

    listening_port = (args.address, args.port)
    print(listening_port)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(listening_port)

    while(True):
        print(udp_socket.recvfrom(1024))


if __name__ == "__main__":
    main()
