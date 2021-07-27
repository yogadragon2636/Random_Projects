# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:57:34 2020

@author: nikpr
"""


import tkinter as tk
from tkinter import ttk

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
        
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
        label = tk.Label(self,text="You made a start page!", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1= tk.Button(self, text = "Visit Page 1", 
                           command = lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2= tk.Button(self, text = "Visit Page 2", 
                           command = lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        button3= tk.Button(self, text = "Dice Roll Page", 
                           command = lambda: controller.show_frame(PageThree))
        button3.pack()
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page_One", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1= tk.Button(self, text = "Back to Home", 
                           command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2= tk.Button(self, text = "go to page two", 
                           command = lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page_Two", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1= tk.Button(self, text = "Back to Home", 
                           command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2= tk.Button(self, text = "go to page one", 
                           command = lambda: controller.show_frame(PageOne))
        button2.pack()

class PageThree(tk.Frame):
    
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