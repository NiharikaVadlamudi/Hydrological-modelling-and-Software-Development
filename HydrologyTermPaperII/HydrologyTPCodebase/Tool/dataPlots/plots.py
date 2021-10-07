import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import csv
from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y-%m-%d")

x=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/dt_res.csv')['time']
# Define the date format

y=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/Model_Codes/data/graph_test_gd.csv')['dis']


y_dt=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/dt_res.csv')['dis']

y_gbr=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/gbr_res.csv')['dis']

y_lin_1=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/lin_1.csv')['dis']

y_lin_2=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/lin_2.csv')['dis']

y_lin_3=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/lin_3.csv')['dis']


y_svr_rbf=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/svr_rbf_res.csv')['dis']
y_svr_lin=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/svr_lin_res.csv')['dis']
y_svr_poly=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/svr_poly_res.csv')['dis']
y_nnet=pd.read_csv('/home/niharika/Desktop/Hydrological_Modelling/Final_Hydro/tool/dataPlots/neural_net_res.csv')['dis']



fig, ax = plt.subplots(figsize=(12,6))
plt.plot(x,y, '-', label='Ground Truth',color='black')
plt.plot(x,y_dt, '--', label='Decision Tree')
plt.plot(x,y_gbr, '--', label='Gradient Boost')
plt.plot(x,y_nnet, '--', label='Neural Net')

plt.plot(x,y_svr_rbf, '--', label='SVR_RBF')
plt.plot(x,y_svr_lin, '--', label='SVR_Linear')
plt.plot(x,y_svr_poly, '--', label='SVR Polynomial')

plt.plot(x,y_lin_1, '--', label='Linear Reg 1')
plt.plot(x,y_lin_2, '--', label='Linear Reg 2')
plt.plot(x,y_lin_3, '--', label='Linear Reg 3')


plt.title('Comparision of ML Models')
plt.ylabel('Predictions')
plt.xlabel('Years')
plt.legend()
plt.show()