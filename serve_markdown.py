
import http.server
import socketserver
import os
import markdown

PORT = 8000

class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".md"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open(self.translate_path(self.path), 'r') as f:
                    content = f.read()
                html = markdown.markdown(content)
                self.wfile.write(b'<html><head><title>Markdown</title></head><body>')
                self.wfile.write(html.encode('utf-8'))
                self.wfile.write(b'</body></html>')
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
    print("serving at port", PORT)
    print("Open your browser and go to http://localhost:8000")
    httpd.serve_forever()
