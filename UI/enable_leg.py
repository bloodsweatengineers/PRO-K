# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller

from tkinter import Label, Entry, Button, Tk, ttk
from tkinter import*
from tkinter import messagebox
import tkinter
##  @package enable_leg
#   Enable leg creates the checkbox which is associated with enabling a specific leg at the top of the UI.

##  The ENABLE_LEG class creates the checkboxes which are, in our case, present at the top of the UI.
class ENABLE_LEG:
    ##  The constructor takes four arguments. Row and column being the geometrical location of the checkbox. tab_nr being the tab where the checkbox should be generated and ID being which leg the checkbox should be identified with
    def __init__(self, row, column, tab_nr, ID):
        self.tab_nr = tab_nr
        self.row = row
        self.column = column
        self.ID = ID
        self.checkbutton_var = IntVar()
        self.checkbutton = Checkbutton(self.tab_nr, text = "Enable {}".format(ID), variable = self.checkbutton_var)
        self.checkbutton.grid(row = self.row, column = self.column ,pady=(10,10))
    ##  The get_data method returns the state of the checkbox.
    def get_data(self):
        return self.checkbutton_var.get()
    ##  The start method disables the state of the checkbox whenever the start button is pressed.
    def start(self):
        self.checkbutton['state'] = DISABLED
    ##  The stop method enables the state of the checkbox whenever the stop button is pressed. 
    def stop(self):
        self.checkbutton['state'] = NORMAL
