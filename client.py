# Dmitriy Kagno 
#!/usr/bin/env python
from socket import *


# Set global variables for HOST and PORT
HOST, PORT = 'localhost', 8080


# Create and send GET request to localhost:8080  
def get(file):

    # initialize GET request and response on function call
    request = f'GET {file} HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n'.encode()
    response = ''
    
    # Create a socket called server_sock 
    with socket(AF_INET, SOCK_STREAM) as server_sock:

        # Try to establish a connection with server lcoated on localhost:8080
        try:
            server_sock.connect((HOST, PORT))

            # Send GET request after connection with server has been established
            server_sock.send(request)

            # Receive data from connected server in 1024 bit chunks
            while True:
                data = server_sock.recv(1024)

                # if the data received from the server is empty stop receiving data
                if not (data):
                    break

                # Append data chunks received from the server to response variable
                response += data.decode()

        # Print error if client fails to connect to server 
        except Exception as e:
            print(e)

        # return aggregated response from server
        return response


# Only perform GET request if this file is manually called
if __name__ == "__main__":

    # Ask user for the file they wish to request
    print("File name for your request: ")
    filename = input()

    # perform GET request with user file input
    response = get(filename)

    # Display final server response in command line
    print(response)