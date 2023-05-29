from tkinter import *
from server import *
from functools import partial
from HistoryText import HistoryText
from ClientObject import ClientObject


class UserInterface(Tk):

    def getTestText(self):
         return 'dsdsd'


    def __init__(self) -> None:
        super().__init__()

        self.__WIDTH = 800
        self.__HEIGHT = 800

        self.listener = None
        
        self.__clientList = None
        self.__serverLogHistoryObj = None

        self.__startUI()

    def __startUI(self):
        self.geometry(f"{self.__WIDTH}x{self.__HEIGHT}")
        self.option_add("*Font","Arial 20 bold")
        self.columnconfigure(0,minsize=800)

        #frame 0
        frame0 = Frame(self)
        createHost_btn = Button(frame0,text='create host',command=self.__onClickCreateHost)
        createHost_btn.pack()

        frame0.grid(row=0,column=0)



        #frame 1
        frame1 = Frame(self,bg='yellow',width=50)

        self.__ui_clientcount = Label(frame1,text=f"client : Null")
        self.__ui_clientcount.pack(padx=5,pady=5)

        # self.__ui_btnTest = Button(frame1,text="CLICK Test",fg="white",bg="blue",command=self.serverOnclickTest)
        # self.__ui_btnTest.pack(padx=5,pady=5)

        frame1.grid(row=1,column=0,padx=5,pady=1)

        #frame 2
        frame2 = Frame(self,bg='green')

        self.__ui_history = Label(frame2,font=("Arial",12,"bold"), height=10, width=70)
        self.__ui_history.pack(padx=5,pady=5,side=TOP, fill=BOTH, expand=True)

        frame2.grid(row=2,column=0,padx=5,pady=1)

        #frame 3
        self.frame3 = Frame(self,bg='blue')
        self.frame3.grid_columnconfigure(0,minsize=300)
        self.frame3.grid_columnconfigure(1,minsize=10)
        self.frame3.grid(row=3,column=0,padx=5,pady=1)

        self.__updateUI()

    def __updateUI(self):
        self.after(1000,self.__updateUI)
        
        if self.listener != None:
            self.__onUpdateUI()

        if self.__clientList:
            self.__ui_clientcount.configure(text=f"client : {len(self.__clientList)}")


        #------------------------------------- update log -------------------------

        self.__ui_history.config(text=self.__serverLogHistoryObj)
        

        #------------------------------------- update user -------------------------
        

        
        
        i = 0
        for client in self.__clientList if self.__clientList != None else range(0):
            
            space = Frame(self.frame3,width=100,bg='#FF00F2')
            space.columnconfigure(3,minsize=20)

            l_name = Label(space,text=client.NAME,bg='#00d9F0' if i % 2 == 0 else '#FFF222',width=10)
            l_name.grid(row=0,column=0)

        

            b_send = Button(space,text='Send',bg='blue',fg='white',command=partial(self.__onClickSend,client) )
            b_send.grid(row=0,column=2)
        
            b_kick = Button(space,text='Kick',bg='red',fg='white',command=partial(self.__onClickKick,client ))
            b_kick.grid(row=0,column=1)

            space.grid(row=i,column=0)

            i+=1


            
        


    def setClientList(self,clientList):
        self.__clientList = clientList

    def setServerHistory(self,serverLogHistoryList):
        self.__serverLogHistoryObj = serverLogHistoryList
        
    def setEventListener(self,listener):
        self.listener = listener


    def __onClickCreateHost(self):
        self.listener.onClickCreateHost()

    def __onUpdateUI(self):
        self.listener.onUpdateUI()

    def __onClickSend(self,client):
        self.listener.onClickSend()

    def __onClickKick(self,client):
        self.listener.onClickKick(client)



        
