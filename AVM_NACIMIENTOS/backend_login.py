from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import sqlite3

class SimpleLoginHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers.get('Content-Length'))
            body = self.rfile.read(length).decode()
            data = urllib.parse.parse_qs(body)
            usuario = data.get('usuario', [''])[0]
            contrasena = data.get('contrasena', [''])[0]

            conn = sqlite3.connect("avm_base.sqlite")
            cursor = conn.cursor()
            cursor.execute("SELECT tipo FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
            row = cursor.fetchone()
            conn.close()

            if row:
                destino = "usuario.html" if row[0] == "usuario" else "admin.html"
                self.send_response(303)
                self.send_header("Location", "/" + destino)
                self.end_headers()
            else:
                self.send_response(303)
                self.send_header("Location", "/index.html")
                self.end_headers()

    def do_GET(self):
        try:
            with open("templates/" + self.path[1:], "rb") as file:
                self.send_response(200)
                if self.path.endswith(".html"):
                    self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Archivo no encontrado")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleLoginHandler)
    print("Servidor corriendo en http://localhost:8000")
    server.serve_forever()