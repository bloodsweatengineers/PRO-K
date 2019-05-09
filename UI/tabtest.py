#Create Tabbed widget in Python GUI Application  
import tkinter as tk  
from tkinter import ttk  
win = tk.Tk()  

win.title("Python GUI App")  
#Create Tab Control  
tabControl=ttk.Notebook(win)  

#Tab1  
tab1=ttk.Frame(tabControl)  
tabControl.add(tab1, text='Tab 1')  

#Tab2  
tab2=ttk.Frame(tabControl)  
tabControl.add(tab2, text='Tab 2')  
tabControl.pack(expand=1, fill="both")  

#Tab Name Labels  
ttk.Label(tab1, text="This is Tab 1").grid(column=0,row=0,padx=10,pady=10)  
ttk.Label(tab2, text="This is Tab 2").grid(column=0,row=0,padx=10,pady=10)  

#Calling Main()  
win.mainloop()
