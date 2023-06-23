import socketserver
from http.server import SimpleHTTPRequestHandler as SimpleHander
from e1_dataprovider import DataProvider

class ServerHandler(SimpleHander):

    def do_GET(self) -> None:
        path = self.path.split('/')
        if path[1] == "data":
            try:
                self.send_header('Content-Type', 'application/json')
                dp = DataProvider(param=path[2:], path="/Users/timniemeijer/programming_2/Assignment_week4/dSST.csv")
                self.send_response(200)
                self.wfile.write(dp.data.encode('utf-8'))
                self.end_headers()
            except ValueError:
                self.send_error(400)
        else:
            self.send_error(404)


def main():
    port = 9000
    socketserver.TCPServer.allow_reuse_address = True
    http = socketserver.TCPServer(("", port), ServerHandler)
    
    print("serving at port", port)
    http.serve_forever()

if __name__ == "__main__":
    main()

