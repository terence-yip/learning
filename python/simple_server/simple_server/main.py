#!/usr/bin/python3

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = 'response' + self.rfile.read(content_len)
        print(post_body)
        self.wfile.write(post_body)
        
def run(server_class=HTTPServer, handler_class=S, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    print("HELLO")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
p = '''
import http.server

def main():
    server_class = http.server.HTTPServer
    handler_class = http.server.SimpleHTTPRequestHandler
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
'''