class Community:


    def __init__(self) -> None:
        pass

    def onClientRecvMessage(self,text):
        if text.find('=') != -1:
            command,value = text.split('=')
            # value = text.split("=")[1]
            print(f'command = {command}\tvalue = {value}')
        
