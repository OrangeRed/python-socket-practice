# Dmitriy Kagno
#!/usr/bin/env python
from socket import *


# Set global variables for HOST and PORT
HOST, PORT = 'localhost', 8080


# Create a socket called server_sock and listen for connections on 'localhost:8080' 
with socket(AF_INET, SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(5)
    print(f"Listening on port {PORT}")
    while True:
      
        # Try to establish a connection with client and acquire request data
        try:
            client_sock, client_addr = server_sock.accept()
            request = client_sock.recv(1024).decode()

            # Split request data into headers and extract filename from headers
            headers = request.split('\n')
            filename = headers[0].split()[1]

            # remove leading '/' to allow for URL variables
            if filename[0] == '/' and len(filename) > 1:
                filename = filename[1:]

            # Try to open the filename extracted from request data 
            try:
                file = open(filename, 'rt')
                content = file.read()
                file.close()

                # If the filename exists then return code 200 along with the file contents
                response = 'HTTP/1.1 200\n\n' + content

                # if the filename does not exist then return code 404 File not found
            except:
                response = 'HTTP/1.1 404\n\nFile not found'

            # Send HTTP response back to the connected client and close the connection
            client_sock.send(response.encode())
            client_sock.close()

            # if the connection with the client fails return the print the error on the server
        except Exception as e:
            print(e)

