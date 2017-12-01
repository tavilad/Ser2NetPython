import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   #c.close()                # Close the connection
   try:
      output = 'Thank you for connecting'
      c.sendall(output.encode())
      data=c.recv(1024)
      if data=="EXIT":
         c.close()
         
   except socket.error:
      c.close()
      
   
