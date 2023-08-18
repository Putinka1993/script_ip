
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
        self.btn.bind('<Button-1>',lambda e, f = "Verdana": self.click(e, f))
        self.label = ttk.Label()
        self.label.pack(anchor=NW, padx=6, pady=6)
        
        self.btn2 = ttk.Button(text="stop", command=self.stop_program)
        self.btn2.pack(anchor=NW, padx=6, pady=7)
        self.btn2.bind('<Return>',lambda e, f = "Verdana": self.stop_program(e, f))
        self.btn2.bind('<Button-1>',lambda e, f = "Verdana": self.stop_program(e, f))
        
        self.root.mainloop()
        
    def click (self, e, f):   
        self.flag = True   
        hostname = self.entry.get()
        #count = 0
        while self.flag:
            response = os.system("ping -c 1 " + hostname)
            if response == 0:
                self.label["text"] = "online"
                #print(count)
            else:
                self.label["text"] = "offline"
            self.root.update()
            time.sleep(3)
            #count += 1
    #window.destroy()
    
    def stop_program(self):
        self.flag = False

app()