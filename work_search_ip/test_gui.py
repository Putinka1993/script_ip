
from tkinter import *
from tkinter import ttk
import os
import tkinter as tk
import time

class app(tk.Frame):
    def __init__(self):
        self.root = Tk()
        self.root.title("track ip")
        self.root.geometry("250x200") 
        
        self.entry = ttk.Entry()
        self.entry.pack(anchor=NW, padx=6, pady=6)      
        self.btn = ttk.Button(text="search ip", command=self.click)
        self.btn.pack(anchor=NW, padx=6, pady=6)
        self.btn.bind('<Return>',lambda e, f = "Verdana": self.click(e, f))
        self.label = ttk.Label(text="write ip")
        self.label.pack(anchor=NW, padx=6, pady=6)

        
        self.root.mainloop()

    def click (self, e, f):      
        hostname = self.entry.get()
        
        for i in range(10):
            time.sleep(5)
            self.response = os.system("ping -c 1 " + hostname)
            if self.response == 0:
                self.label.config(text = str("online"))  
            else:
                self.label.config(text = str("offline"))
            self.root.update()

    
    

    #window.destroy()
    


#search_ip = "test"

app()
