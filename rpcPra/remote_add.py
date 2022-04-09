from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl
import json
host = ("", 8003)

class AddHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        print("parsed_url = ", parsed_url)
        qs = dict(parse_qsl(parsed_url.query))
        print("qs = ", qs)
        a = int(qs.get("a", 0))
        b = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "result": a + b
        }).encode("utf-8"))

if __name__ == '__main__':
    server = HTTPServer(host, AddHandler)
    server.serve_forever()


