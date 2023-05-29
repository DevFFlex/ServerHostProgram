from tkinter import simpledialog
from tkinter import *

class InputDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Input Dialog")
        self.label = Label(master, text="Enter text:")
        self.label.pack()
        self.entry = Entry(master)
        self.entry.pack()
        return self.entry # Return the Entry widget for focus

    def apply(self):
        value = self.entry.get()
        self.result = value
