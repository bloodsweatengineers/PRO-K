from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter

class ENABLE_LEG:
    def __init__(self, row, column, tab_nr, ID):
        self.tab_nr = tab_nr
        self.row = row
        self.column = column
        self.ID = ID
        self.checkbutton_var = IntVar()
        self.checkbutton = Checkbutton(self.tab_nr, text = "Enable {}".format(ID), variable = self.checkbutton_var)
        self.checkbutton.grid(row = self.row, column = self.column ,pady=(10,10))

    def get_data(self):
        return self.checkbutton_var.get()

    def start(self):
        self.checkbutton['state'] = DISABLED

    def update(self):
        return 0

    def stop(self):
        self.checkbutton['state'] = NORMAL

