#!/usr/bin/python
import os
import udp_message_sender
import json_message_loader
import message_encoder


def main():
    messages_path = os.getcwd() + "/messages.json"
    address = "127.0.0.1"
    port = 50000

    message_loader = json_message_loader.json_message_loader()
    json_messages = message_loader.load_messages(messages_path)

    encoder = message_encoder.message_encoder()
    messages = encoder.encode(json_messages)

    message_sender = udp_message_sender.udp_message_sender()
    for message in messages:
        message_sender.send_message(message, address, port)


if __name__ == "__main__":
    main()
