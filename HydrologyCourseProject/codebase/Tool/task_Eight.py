import tkinter as tk
import tkinter.filedialog as tkfd
import pandas as pd
from tkinter import *
from selectPage import SelectPage
from vars import Vars


import tkinter as tk
import tkinter.filedialog as tkfd
from tkinter import *
from selectPage import SelectPage
from vars import Vars
from tkinter import ttk 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import joblib
import os 
import xarray as xr
import matplotlib

from WM_climate_indices import *
from process_csv import *



class DroughtIndex(SelectPage):

    def __init__(self,parent,controller):
        SelectPage.__init__(self, parent, controller)
        
        #Set of Label-Entry Lists
        self.nameField={}
        self.entryField={}

        self.calValue=tk.StringVar()
        self.calValue.set("Not Calculated")
        
        
        self.indexLabel = ttk.Label(self, text = 'Select the Index : ', 
                        font = Vars.SMALL_FONT)

        self.indexType = tk.StringVar()
        self.indexChosen = ttk.Combobox(self, width = 15, textvariable = self.indexType)
        self.indexChosen['values'] = (
            'SPI',
            'SPEI',
        )        

        self.indexLabel.place(x = 50, y = 100)
        self.indexChosen.place(x = 50, y = 130)


        self.scaleLabel = ttk.Label(self, text = 'Select the Time-Scale : ', 
                        font =Vars.SMALL_FONT)

        self.scaleType = tk.IntVar()
        self.scaleChosen = ttk.Combobox(self, width = 15, textvariable = self.scaleType)
        self.scaleChosen['values'] = (
            3,
            6,
            9,
            12
        )        

        self.indexLabel.place(x = 50, y = 100)
        self.indexChosen.place(x = 50, y = 130)

        
        self.scaleLabel.place(x = 50, y = 180)
        self.scaleChosen.place(x = 50, y = 210)

        self.optViewer=tk.Label(self,textvariable=self.calValue,fg=Vars.FG,bg=Vars.BG,font=Vars.LARGE_FONT)
        self.optViewer.place(x=300,y=500)

        # # Input Label-Entry-Submit 
        self.fileInput=tk.Entry(self)
        self.fileInput.place(x=50,y=300,w=200)
        self.inputLabel = ttk.Label(self, text = 'Select the Input File : ', 
                        font = Vars.SMALL_FONT)
        self.chooseFile=tk.Button(self,text='Input File',command=lambda:self.openFile(),padx=10,pady=10)
        
        self.inputLabel.place(x = 50, y = 260)
        self.chooseFile.place(x=290,y=300,height =20, width=125)

        #Output-Label-Entry-Submit
        self.outputLabel = ttk.Label(self, text = 'Provide Output file name ', 
                        font = Vars.SMALL_FONT)
        
        self.outputLabel.place(x=50, y = 350)
        self.fileOutput=tk.Entry(self)
        self.fileOutput.place(x=50,y=380,w=200)
        

        self.calculate2=tk.Button(self,text='Calculate',command=lambda:self.doprocessing(),padx=10,pady=10)
        self.calculate2.place(x=50,y=420,w=125,height=35)

        btn4=tk.Button(self, text="Show Visualizations", fg='black', command = self.show_visuals, font = ("Helvetica",10))
        # btn4.place(row = 13, column = 1,sticky="w")
        # btn4.grid_forget()
        self.btn4 = btn4
    
    def show_visuals(self):
        print ("showing visuals")
        if self.task == 'SPI':
            plt.plot( self.output_df['SPI'])
            plt.show()
        elif self.task == 'SPEI':
            plt.plot( self.output_df['SPEI'])
            plt.show()
        else:
            plt.plot( self.output_df['SPI'])
            plt.show()
    
    
    def doprocessing(self):
        filepath = self.fileInput.get()
        task = self.indexType.get()
        self.task = task
        
        print (task)

        time = int(self.scaleType.get())
        print (time)
        self.time = time
        if task == 'SPI':
            self.output_df = process_csv.process(filepath, self.fileOutput.get(), "SPI",time)
        elif task == 'SPEI':
            self.output_df = process_csv.process(filepath,self.fileOutput.get(),"SPEI",time)
        elif task == 'SPAEI':
            self.output_df = process_csv.process(filepath,self.fileOutput.get(),"SPAEI",time)

        self.btn4.place(x = 50, y = 600)

    # Functions (in above commands)
    def openFile(self):
        fileName=tkfd.askopenfilename(filetypes =[('CSV Files', '*.csv')])
        if fileName!=() and fileName !="" : 
            self.fileInput.delete(0,tk.END)
            self.fileInput.insert(0,fileName)
    
  