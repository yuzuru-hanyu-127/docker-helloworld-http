import http.server
import socketserver

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        with open('./index.html', 'rb') as f:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f.read())
            return

    def do_HEAD(self):
        with open('./index.html', 'rb') as f:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f.read())
            return

httpd = socketserver.TCPServer(("", 80), CustomRequestHandler)
httpd.serve_forever()
