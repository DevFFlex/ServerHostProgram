import socket

class ClientObject:
    def __init__(self,client_socket : socket.socket,addr : tuple,name : str):
        self.NAME : str = name
        self.CLIENT : socket.socket = client_socket
        self.Address : tuple = addr
        self.status_alive = True

    def getName(self) -> str:
        return self.NAME
    
    def getClientSocket(self) -> socket.socket:
        return self.CLIENT
    
    def getAddress(self) -> tuple:
        return self.Address
    
    def isAlive(self) -> bool:
        return self.status_alive