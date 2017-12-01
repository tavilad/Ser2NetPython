from tkinter import *
from Client import *

#make an empty window
root = Tk()

#make the main window frame
frame = Frame(root)
frame.pack()

#pressing this button makes the connection of the client to the TCP/IP Server
connectBtn = Button(frame, text="Connect")
connectBtn.bind("<Button-1>", printme)
connectBtn.pack()

root.mainloop()
