#Standard modules
import socketserver
from http.server import SimpleHTTPRequestHandler as SimpleHandler
import json
#Local modules
from e1_dataprovider import DataProvider


class ServerHandler(SimpleHandler):

    def do_GET(self) -> None:
        path = self.path.split('/')
        if path[1] == "data":
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                dp = DataProvider(param=path[2:], path="/Users/timniemeijer/programming_2/Assignment_week4/dSST.csv") # magic string, but ok
                data_json = json.dumps(dp.data)  # Convert data to JSON string
                self.wfile.write(data_json.encode('utf-8'))  # Write JSON string to client
            except ValueError:
                # Good to have a difference between 404 and 400
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

