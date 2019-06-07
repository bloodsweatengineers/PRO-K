# Kerim Kilic
# 16024141
# De Haagse Hogeschool
# PRO-K: PWM Controller


import user_interface
from tkinter import Tk
##  @package main
#   This module acts as the main for the user interface. The only function it has is looping the user interface

root = Tk()
gui = user_interface.GUI(root)

root.mainloop()
