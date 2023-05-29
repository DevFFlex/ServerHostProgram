import sys
import os
import json
import time
import threading
import socket
from tkinter import *
from server import *
from HistoryText import HistoryText
from ClientObject import ClientObject
from Community import Community


class ClientDataList:
    
    def __init__(self) -> None:
        self.__clients_list = []

    def getList(self) -> list:
        return self.__clients_list
    
    def getCount(self) -> int:
        return len(self.__clients_list)
    

    def addClient(self,client):
        self.__clients_list.append(client)

    def clearClient(self):
        self.__clients_list.clear()



class Server():

    def log(self,strr):
        self.historyTextServer.addHistory(strr)
        print(strr)

    def __init__(self):
        self.historyTextServer = HistoryText(name='ServerLog')
        self.clientDataList = ClientDataList()
        self.community = Community()
        self.__ui = None
        self.isrun = False


    def setUserInterface(self,ui):
        self.__ui = ui
        
    def createHost(self,ip = '192.168.1.19',port = 5000):
        try:
            self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__server_socket.bind((ip, port))
            self.__server_socket.listen(1)
            self.log(f'Create Server {ip} port {port}')
            self.log('Server listening..............')
            

            self.isrun = True
            self.__passCreateHost = True
        except:
            self.__passCreateHost = False

        if self.__passCreateHost:
            threading.Thread(target=self.__listenClient).start()
        else:
            self.log('Host ไม่ได้เปิด')
        
        self.log("----------------------------------------")

    
    def __listenClient(self):

        while self.isRun(): 

            client_socket, client_address = self.__server_socket.accept()
            if not client_socket:
                continue

            
            try:
                data = client_socket.recv(1024)
                if data:
                    client_name = data.decode('utf-8')
            except:
                client_name = "NULL"
            
            self.log(f'{client_name} join server')

            client_obj = ClientObject(client_socket=client_socket,addr=client_address,name=client_name)
            
            self.clientDataList.addClient(client_obj)

            threading.Thread(target=self.__recvAndResponseClient,args=(client_obj,)).start()
            


    def __recvAndResponseClient(self,clientobject : ClientObject):
        while clientobject.isAlive():
            try:
                data = clientobject.CLIENT.recv(1024)
                if data:
                    data_str = data.decode('utf-8')
                    print(data_str)
                    # self.printOUT(data_str)
                    self.community.onClientRecvMessage(data_str)
                    
                    
            except Exception as e:
                self.log(f"Error receiving data: {e}")
                # print("SERVER-RECV-ERROR")
                pass

                
    def send2Client(self,client : ClientObject,text : str,endKey = '$'):
        client.CLIENT.send(f'{text}{endKey}'.encode('utf-8'))

        

    def closeServer(self):
        self.__server_socket.close()
        self.clientDataList.clearClient()
        self.isrun = False
        self.__server_socket.connect_ex()























