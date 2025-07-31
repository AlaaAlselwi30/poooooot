import http.server
import socketserver
import socket

# Get your IP address
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Create a web server and define the handler to manage the
# incoming request
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP socket server
with socketserver.TCPServer((IPAddr, 8080), Handler) as httpd:

    print("serving at port", IPAddr, 8080)

    # Wait forever for incoming http requests
    httpd.serve_forever()