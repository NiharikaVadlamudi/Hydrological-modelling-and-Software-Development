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


# Task specific libraries 
import joblib
from scipy.stats import moment
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error as MSE

#File specific 
from scalers import sc_X,sc_y


neuralNet=joblib.load('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/Model_Codes/model_files/Neural_Net.sav')

class NeuralNet(SelectPage):
    def __init__(self, parent, controller):
          
        global sc_X,sc_y
        self.scalerx=sc_X
        self.scalery=sc_y
  

        self.cp='Convective Prepitation'
        self.lsp='Large Scale Preciptation'
        self.swvl1='Soil Volumetric Layer 1'
        self.ro='Runoff'
        self.sd='Snow Depth'

        self.options= ["Linear","RBF","Polynomial"]
        self.words=[self.cp,self.lsp,self.swvl1,self.ro,self.sd]


        self.textFields = {}
        self.labelFields = {}

        self.cal_value = tk.StringVar()
        self.cal_value.set("N/A")

        # _,_,self.scalerx,self.scalery=self.preProcessing(trainframe)


        SelectPage.__init__(self, parent, controller)
        
        self.label_name=tk.Label(self, text = "Neural Network", font = Vars.LARGE_FONT,bg='cyan')
        self.label_name.place(x=100,y=120)


        for idx, i in enumerate(self.words):
            self.labelFields[i] = tk.Label(self, text = i, font = Vars.LABEL_FONT)
            self.textFields[i] = tk.Entry(self, validate='key',vcmd=(controller.register(self.validate_float), '%P'))
            self.labelFields[i].place(x =500, y = 50*(idx!=0)+ 60*(idx==0)+(50* idx))
            self.textFields[i].place(x = 700, y = 50*(idx!=0) + 60*(idx==0)+(50 * idx),w=150)


        self.calculate = tk.Button(self, text = "Calculate", 
        command =  lambda: self.vec_predict(),bg='white')
        self.calculate.place(x =500, y = 350, width =180, height =40)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = Vars.LABEL_FONT,bg='cyan')
        self.curr_value.place(x =500, y = 450,width =160,height =40)

        # CSV File
        self.csv_text = tk.StringVar()

        self.csv_text.set("CSV File Upload : ")
        self.csv_label = tk.Label(self, textvariable = self.csv_text, font = Vars.LABEL_FONT,padx = 10,pady = 10)
        self.csv_label.place(x = 100, y = 250,h=40)

        self.fileInput = tk.Entry(self)
        self.fileInput.place(x = 100, y = 300)

        self.chooseFile = tk.Button(self, text = "Input File", 
        command =  lambda: self.open_file(), padx = 10,pady = 10)
        self.chooseFile.place(x=275, y = 250, width = 125, height = 40)

        #Label 
        self.output_label=ttk.Label(self, text = "Output File Name :", font =Vars.LABEL_FONT)
        self.output_label.place(x=100,y=350,w=200,h=40) 

        self.fileOutput = tk.Entry(self)
        self.fileOutput.place(x =100, y =400, w = 200)


        self.calculate2 = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_csv_output(), padx = 10,pady = 10)
        self.calculate2.place(x =150, y = 470, width = 100, height = 30)

    
    def preProcessing(self,dataframe):
            #Split into X
            #Scale them
            df1=dataframe[['cp','lsp','swvl1','ro','sd']]
            X = df1.iloc[:,:5].values.astype(float)
            X=np.reshape(X,(-1,5))
            return(X)


    
    def validate_float(self, inp, empty = 0):
        try:
            if inp != "" or empty:
                float(inp)
        except:
            return False
        return True
    

    def open_file(self):
        filename = tkfd.askopenfilename(filetypes =[('CSV Files', '*.csv')])
        if filename != () and filename != "":
            self.fileInput.delete(0, tk.END)
            self.fileInput.insert(0, filename)

        
    def _calculate_csv_output(self):
        inputFilename = self.fileInput.get()
        outputFilename = self.fileOutput.get()
        if inputFilename == "" or outputFilename == "":
            self.csv_text.set("Invalid File")
        else:
            self.df=pd.read_csv(inputFilename)
            self.df_copy=self.df.copy()
            data=self.preProcessing(self.df)
            y_pred=self.scalery.inverse_transform((neuralNet.predict(self.scalerx.transform(data))))            
            
            result=self.df_copy.copy()
            result['dis']=y_pred
            result.to_csv(outputFilename,index=False)

        self.csv_text.set("Done!")
        self.fileInput.delete(0,tk.END)
        self.fileOutput.delete(0,tk.END)
            

    def vec_predict(self):
        validate=True
        for i in self.words:
            validate=validate and self.validate_float(self.textFields[i].get(),1)
        vec=[]
        if validate:
            for i in self.words:
                vec.append(float(self.textFields[i].get()))
            vec=np.asarray(vec).reshape(-1,5)
            #Predict it
            y_pred=self.scalery.inverse_transform((neuralNet.predict(self.scalerx.transform(vec))))
            self.cal_value.set(y_pred)    
        
        else:
            self.cal_value.set('Missing Inputs')
        


        



  



        
       