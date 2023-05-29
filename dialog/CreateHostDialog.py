from tkinter import Misc, simpledialog
from tkinter import *

class CreateHostDialog(simpledialog.Dialog):


    def body(self, master):
        self.title("CreateHost")

        self.label1 = Label(master, text="IP Address :")
        self.label1.pack()
        self.entry1 = Entry(master)
        self.entry1.pack()

        self.label1 = Label(master, text="Port :")
        self.label1.pack()
        self.entry2 = Entry(master)
        self.entry2.pack()



        # return self.entry # Return the Entry widget for focus/

    def apply(self):
        ip = self.entry1.get()
        port = self.entry2.get()
        self.result = {"IP":ip,"PORT":port}