from tkinter import *
from server import *
from UserInterface import *
from EventListener import EventListener



if __name__ == "__main__":

    

    server = Server()
    # server.createHost('192.168.1.19',5000)

    
    serverUserInterface = UserInterface()

    eventListener = EventListener()
    eventListener.setServer(server)
    eventListener.setUserInterface(serverUserInterface)


    serverUserInterface.setEventListener(eventListener)
    serverUserInterface.mainloop()

    exit()