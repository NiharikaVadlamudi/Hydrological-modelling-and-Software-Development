#Importing all libraries 
import os 
import csv
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import joblib 
import sklearn 
from sklearn.preprocessing import StandardScaler


sc_X = StandardScaler()
sc_y = StandardScaler()

trainFile='/home/niharika/Desktop/4_2/RR/Hydrological_Modelling/Final_Hydro/tool/train.csv'
dataframe=pd.read_csv(trainFile)

def preProcessing(dataframe):
    #Split into X,y 
    #Scale them
    df1=dataframe[['cp','e','ilspf','lsp','pev','tcrw','tp','swvl1','swvl2','ro']]
    X = df1.iloc[:,:8].values.astype(float)
    y = df1.iloc[:,-1].values.astype(float)
    X=np.reshape(X,(-1,8))
    y=np.reshape(y,(-1,1))
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)
    return(X,y,sc_X,sc_y)

X,y,sc_X,sc_y=preProcessing(dataframe)
