import user_interface
from tkinter import Tk

root = Tk()
this_gui = user_interface.GUI(root)

while True:
    root.update_idletasks()
    root.update()

