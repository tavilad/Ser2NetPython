import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Close the socket when done





def printme(event):
    print("test")
    return;

def connect(event):
    global s
    global host
    global port
    s.connect((host, port))
    return;


def disconnect(event):
    global s
    cmd="EXIT"
    s.sendall(cmd.encode())
    s.close()
    s = socket.socket()         # Create a socket object
    print("socket closed")
    return;

def printFromSocket(event):
    global s
    print (s.recv(1024))
    return;
    


    
    
