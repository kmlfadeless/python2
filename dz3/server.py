import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from dz3.jim.utils import get_message, send_message
from dz3.jim.config import *


def message_response(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and isinstance(message[TIME], float):
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'Incorrect request'}


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = ''

    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Port should be an integer number')
        sys.exit(0)

    server.bind((addr, port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        message = get_message(client)
        print(message)
        response = message_response(message)
        send_message(client, response)
        client.close()

