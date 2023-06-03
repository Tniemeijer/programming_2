import socketserver
from http.server import SimpleHTTPRequestHandler as SimpleHander
from e1_dataprovider import DataProvider

class ServerHandler(SimpleHander):
    def do_GET(self) -> None:
        path = self.path.split('/')
        if path[1] == "DATA":
            try:
                dp = DataProvider(param=path[2], path=data_path)
                self.send_header('Content-Type', 'application/json')
                self.send_response(200)
                self.wfile.write(dp.data.encode(encoding='utf_8'))
                self.end_headers()
            except ValueError:
                self.send_error(400)
        else:
            self.send_error(404)
        super().do_GET()

port = 9000

socketserver.TCPServer.allow_reuse_address = True
http = socketserver.TCPServer(("", port), ServerHandler)
data_path = "DATA/dSST.csv"

print("serving at port", port)
http.serve_forever()
