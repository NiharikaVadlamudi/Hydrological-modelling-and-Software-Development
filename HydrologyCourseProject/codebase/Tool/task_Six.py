import tkinter as tk 
from tkinter import ttk
import matplotlib.pyplot as plt 
import numpy as np
import os
import math
from math import exp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter.filedialog as tkfd
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import matplotlib.image as mpimg
import cv2

import tkinter as tk
import tkinter.filedialog as tkfd
from tkinter import *
from selectPage import SelectPage
from vars import Vars
from tkinter import ttk 

# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.axes import Subplot




import pickle

import pandas as pd

class BoxPlotAnalysis(SelectPage):

    def __init__(self,parent,controller):
        SelectPage.__init__(self, parent, controller)
        boxPlot = './boxPlots/plots_box/'

        self.params = (
            'cp',
            'e',
            'ilspf',
            'pev',
            'sp',
            'tcrw',
            'swvl1',
            'swvl2',
            'swvl3',
            'swvl4',
            'ro'
        )

        self.param_list=(
            'Convective Precipitation',
            'Evaporation',
            'ILSPF',
            'Potential Evaporation',
            'Surface Pressure ',
            'Total Rain Water Column',
            'Soil Volumetric Layer 1',
            'Soil Volumteric Layer 2',
            'Soil Volumteric Layer 3 ',
            'Soil Volumteric Layer 4',
            'Runoff')
        
        self.param_dict=dict(zip(self.param_list,self.params))
        

        self.headingLabel = ttk.Label(self, text = 'Runoff Data Analysis', font = Vars.LARGE_FONT)

        self.paramLabel = ttk.Label(self, text = 'Select Parameter : ', 
                        font =Vars.LABEL_FONT)

        self.param = tk.StringVar()
        print('Param Value ' ,tk.StringVar())
        self.paramChosen = ttk.Combobox(self, width = 15,  
                            textvariable = self.param)

        self.paramChosen['values'] = self.param_list

        self.button = tk.Button(self, text = 'Show Box Plot ', width = 25, command = lambda:self.show_boxPlot())
        self.button1=tk.Button(self, text = 'Total Distribution Plot', width = 25, command = lambda:self.show_analysisPlot())


        self.headingLabel.place(x = 50, y = 100)
        self.paramLabel.place(x = 50, y = 150)
        self.paramChosen.place(x= 270, y = 150)
        self.button.place(x = 70, y = 250)  
        self.button1.place(x = 70, y = 300)   



    def show_boxPlot(self):
        image_path = "./boxPlots/plots_box/" + self.param_dict[self.param.get()] + ".png"
        img = mpimg.imread(image_path)
        fig = Figure()
        ax = Subplot(fig, 111)
        fig.add_subplot(ax)
        canvas = FigureCanvasTkAgg(fig, self)

        ax.imshow(img)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)
        canvas._tkcanvas.pack(side=RIGHT)
    
    def show_analysisPlot(self):
        image_path = "./boxPlots/analysisPlots/" + self.param_dict[self.param.get()] + "2"+".png"
        img = mpimg.imread(image_path)
        fig = Figure()
        ax = Subplot(fig, 111)
        fig.add_subplot(ax)
        canvas = FigureCanvasTkAgg(fig, self)

        ax.imshow(img)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)
        canvas._tkcanvas.pack(side=RIGHT)