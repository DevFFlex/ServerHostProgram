from UserInterface import *
from dialog.InputDialogClass import InputDialog
from dialog.CreateHostDialog import CreateHostDialog
from database_devflex.database_class import Database

class EventListener:

    def __init__(self) -> None:
        self.db = Database('option')


    def setServer(self,server):
        self.server = server
    def setUserInterface(self,userInterface):
        self.ui = userInterface


    

    def onUpdateUI(self):
        self.ui.setClientList(self.server.clientDataList.getList())
        self.ui.setServerHistory(self.server.historyTextServer)

    def onClickSend(self,client,text):
        inputDialog = InputDialog(self.ui)
        result = inputDialog.result
        if result != "" and result != None:
            self.server.send2Client(client=client,text=text)
        

    def onClickKick(self,client):
        pass

    def onClickCreateHost(self):
        if self.server.isrun:
            self.server.closeServer()
        else:
            host_dialog = CreateHostDialog(self.ui)
            result = host_dialog.result
            ip = result['IP']
            port = result['PORT']
            if ip != "" and port != "":
                print(f'host ip = {ip}\nport = {port}')
                if str(port).isdigit():
                    self.server.createHost(ip,int(port))
                    self.db.appendData({"IP":ip,"PORT":int(port)})
            else:
                data_default = self.db.getData()
                self.server.createHost(data_default['IP'],data_default['PORT'])
            
        