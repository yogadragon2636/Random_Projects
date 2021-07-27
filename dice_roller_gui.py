# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:57:34 2020

@author: nikpr
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from DieRoller import *


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT=("Verdana", 40)

class GuiWindows(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top",fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
   
         
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Dice Roller Stats", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        Label(StartPage, text = 'Number of Dice:', bg = "white", fg = "black", font = "none 12 bold").grid(row=2, column=0,sticky=W)
        textentry_num = Entry (StartPage, width = 4, bg = "light grey")
        textentry_num.grid(row=2, column = 1, sticky = W)

        Label(StartPage, text = 'Type of Dice:', bg = "white", fg = "black", font = "none 12 bold").grid(row=3, column=0,sticky=W)
        textentry_type = Entry (StartPage, width = 4, bg = "light grey")
        textentry_type.grid(row=3, column = 1, sticky = W)
        
        Label(StartPage, text = 'Number to drop:', bg = "white", fg = "black", font = "none 12 bold").grid(row=4, column=0,sticky=W)
        textentry_drop = Entry (StartPage, width = 4, bg = "light grey")
        textentry_drop.grid(row=4, column = 1, sticky = E)
        
        button1= tk.Button(self, text = "Roll Dice!", 
                           command = lambda: controller.show_frame(PageOne))
        button1.pack()

        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Dice Stats", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1= tk.Button(self, text = "Back to Home", 
                           command = lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure (figsize=(5,5), dpi =100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [5,6,8,2,3,4,5,6])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        
app = GuiWindows()
app.mainloop()