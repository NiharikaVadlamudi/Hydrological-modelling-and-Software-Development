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


import pickle

import pandas as pd

class BoxPlotAnalysis(PageSelect):

    def __init__(self,parent,controller):
        PageSelect.__init__(self, parent, controller)
        boxPlot = './plots_box/'
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

        self.headingLabel = ttk.Label(self, text = 'Runoff data analysis', font = LARGE_FONT)

        self.paramLabel = ttk.Label(self, text = 'Select a parameter : ', 
                        font = SMALL_FONT)

        self.param = tk.StringVar()
        self.paramChosen = ttk.Combobox(self, width = 15,  
                            textvariable = self.param)

        self.paramChosen['values'] = self.params

        self.button = tk.Button(self, text = 'Show Box plot ', width = 25, command = lambda:self.show_boxPlot())
        



        self.headingLabel.place(x = 50, y = 100)
        self.paramLabel.place(x = 50, y = 150)
        self.paramChosen.place(x= 270, y = 150)
        self.button.place(x = 70, y = 200)    



    def show_boxPlot(self):
        image_path = "./plots_box/" + self.param.get() + ".png"
        img = mpimg.imread(image_path)
        imgplot = plt.imshow(img)
        plt.show()