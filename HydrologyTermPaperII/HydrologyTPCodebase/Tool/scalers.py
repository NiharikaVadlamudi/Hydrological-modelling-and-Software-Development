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

trainFile='/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/Model_Codes/data/trainComb.csv'
dataframe=pd.read_csv(trainFile)

def preProcessing(dataframe):
    #Split into X,y 
    #Scale them
    df1=dataframe[['cp','lsp','swvl1','ro','sd','dis']]
    X = df1.iloc[:,:5].values.astype(float)
    y = df1.iloc[:,-1].values.astype(float)
    X=np.reshape(X,(-1,5))
    y=np.reshape(y,(-1,1))
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)
    return(X,y,sc_X,sc_y)

X,y,sc_X,sc_y=preProcessing(dataframe)
