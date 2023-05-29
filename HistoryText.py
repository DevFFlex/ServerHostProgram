
class HistoryText:
    def __init__(self,name : str = None) -> None:
        self.__historyName : str = name
        self.__historylist : list = []
        self.__limite : int = 15

    def addHistory(self,data):
        if len(self.__historylist) > self.__limite:
            self.__historylist.remove(self.__historylist[0])
        self.__historylist.append(data)    

    def getHistory(self) -> list:
        return self.__historylist
    
    def getHistoryName(self) -> str:
        return self.__historyName if not self.__historyName else 'NULL' 
    
    def __str__(self) -> str:
        strout = ''
        for x in self.__historylist:
            strout += x + "\n"
        return strout