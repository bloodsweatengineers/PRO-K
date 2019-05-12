import ui
from tkinter import Tk

root = Tk()
this_gui = ui.GUI(root)

while True:
    root.update_idletasks()
    root.update()

