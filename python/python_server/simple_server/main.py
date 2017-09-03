#!/usr/bin/python3

import http.server

def main():
    server_class = http.server.HTTPServer
    handler_class = http.server.SimpleHTTPRequestHandler
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
