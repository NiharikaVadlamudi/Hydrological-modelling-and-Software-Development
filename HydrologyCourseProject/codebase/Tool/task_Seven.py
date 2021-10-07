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

class GLDAS(SelectPage):
    def __init__(self,parent,controller):
        SelectPage.__init__(self, parent, controller)
        self.headingLabel = ttk.Label(self, text = 'GLDAS Data set analysis', font = Vars.LARGE_FONT)
        self.indexLabel = ttk.Label(self, text = 'Select a index : ', 
                        font =Vars.SMALL_FONT)
        self.index = tk.StringVar()
        self.indexChosen = ttk.Combobox(self, width = 15, textvariable = self.index)

        self.indexChosen['values'] = (
            'SPI',
            'SEPI',
        )
        
        self.scaleLabel = ttk.Label(self, text = 'Select scale : ', 
                        font =Vars.SMALL_FONT)

        self.scale = tk.IntVar()
        self.scaleChosen = ttk.Combobox(self, width = 15, textvariable = self.scale)
        self.scaleChosen['values'] = (
            6,
            12,
        )

        self.distbLabel = ttk.Label(self, text = 'Select a distribution : ', 
                        font = Vars.SMALL_FONT)
        self.distb = tk.StringVar()
        self.distbChosen = ttk.Combobox(self, width = 15, textvariable = self.distb)
        
        self.distbChosen['values'] = (
            'gamma',
            'pearson'
        )

        self.button = tk.Button(self, text = 'Submit', width = 25, command = lambda:self.analysis())

        self.headingLabel.place(x = 50, y = 100)
        self.indexLabel.place(x = 50, y = 150)
        self.indexChosen.place(x = 50, y = 180)

        self.scaleLabel.place(x = 50, y = 240)
        self.scaleChosen.place(x = 50, y = 270)
        
        self.distbLabel.place(x= 50, y = 330)
        self.distbChosen.place(x = 50, y = 360)

        self.bboxLabel = ttk.Label(self, text = 'Enter Bounding Box : ',
                        font =Vars.SMALL_FONT)
        
        self.infoLabel = ttk.Label(self, text = 'Lat - Long', font = Vars.SMALL_FONT)

        self.bbox1 = tk.Entry(self)
        self.bbox2 = tk.Entry(self)
        self.bbox3 = tk.Entry(self)
        self.bbox4 = tk.Entry(self)

        self.bboxLabel.place(x = 50, y = 420)
        self.bbox1.place(x = 50, y = 450, w = 30)
        self.bbox2.place(x = 90, y = 450, w = 30)
        self.bbox3.place(x=130, y = 450, w = 30)
        self.bbox4.place(x = 170, y = 450, w = 30)
        self.infoLabel.place(x = 220, y = 450)

        self.button.place(x = 50, y = 490)
    def analysis(self):
        bbox = [0,0,0,0]
        bbox[0] = int(self.bbox1.get())
        bbox[1] = int(self.bbox2.get())
        bbox[2] = int(self.bbox3.get())
        bbox[3] = int(self.bbox4.get())
        WM_climate_indices.climate_indices_max(index = self.index.get(),dataset_name="data/GLDAS2.0_TP_global.nc", dataset_type= "GLDAS",\
            scales = self.scale.get(), distribution= self.distb.get(), bounding_box= bbox)