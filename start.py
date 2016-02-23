from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(b'Hello my friend!!')

serv = HTTPServer(("localhost", 80), HttpProcessor)
serv.serve_forever()