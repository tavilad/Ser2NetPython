import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.






def printme(event):
    print("test")
    return;

def connect(event):
    s.connect((host, port))
    return;


def disconnect(event):
    s.close()                     # Close the socket when done
    return;

def printFromSocket(event):
    print (s.recv(1024))
    return;
    


    
    
