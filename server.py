#!/usr/bin/env python

import logging
# from http.server import BaseHTTPRequestHandler, HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request \nFile: %s\nHeaders:\n%s", str(self.path), str(self.headers))
        if files.get(self.path, None) is not None:
            self.send_response(200, 'OK')
            self.wfile.write(files[self.path])
        else:
            self.send_response(404, "NOT FOUND")
        self._set_headers()

    def do_DELETE(self):
        logging.info("DELETE request\nFile: %s\nHeaders:\n%s", str(self.path), str(self.headers))
        files[self.path] = None
        self.send_response(204, "NO CONTENT")
        self._set_headers()

    def do_PUT(self):
        content_len = int(self.headers.get('Content-Length'))
        content = self.rfile.read(content_len)
        logging.info("PUT request\nPath: %s\nHeaders:\n%sBody:\n%s\n", str(self.path), str(self.headers)[:-1], content.decode("utf-8"))
        files[self.path] = content
        self.send_response(201, "CREATED")
        self._set_headers()


if __name__ == "__main__":
    files = {}
    logging.basicConfig(filename="/var/log/server.log", level=logging.INFO)
    server_address = ("127.0.0.1", 8080)
    httpd = HTTPServer(server_address, HandleRequests)
    httpd.serve_forever()
