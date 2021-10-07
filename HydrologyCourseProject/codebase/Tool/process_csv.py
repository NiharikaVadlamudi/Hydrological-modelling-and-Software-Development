# from ml_models import model_weights
# import indian_standards
# import weighted_average
import pandas as pd
from spi_index import spi
from spei_index import spei
import os
import numpy as np
import scipy.io
def process(input_csv_path, output_csv_path, choice, time):
    print ("processing to csv")
    df = pd.read_csv(input_csv_path)
    df.head()
    output_df = pd.DataFrame()
    if choice == "SPI":
        # output_df = pd.DataFrame(columns=["pH", "temperature", "turbidity", "tds", "nitrates", "coliform", "wqi", "wqc"]) 
        if "precipitation" in df.keys() and "YEAR" in df.keys():
            average_precip = df['precipitation'].mean()
            df['precipitation'] = df['precipitation'].fillna(average_precip)

            out = spi(df['precipitation'],time,df['YEAR'].iloc[0],df['YEAR'].iloc[0],df['YEAR'].iloc[-1])
            output_df['YEAR'] = df['YEAR']
            output_df['SPI'] = out
            output_df.drop(output_df.index[np.arange(0,time-1)],inplace=True)

    elif choice == "SPEI":
        # output_df = pd.DataFrame(columns=["pH", "temperature", "turbidity", "tds", "nitrates", "coliform", "wqi", "wqc"]) 
        if "precipitation" in df.keys() and "YEAR" in df.keys() and "PET" in df.keys():
            average_precip = df['precipitation'].mean()
            average_pet = df['PET'].mean()
            df['precipitation'] = df['precipitation'].fillna(average_precip)
            df['PET'] = df['PET'].fillna(average_pet)
            out = spei(df['precipitation'],df['PET'],time,df['YEAR'].iloc[0],df['YEAR'].iloc[0],df['YEAR'].iloc[-1])
            output_df['YEAR'] = df['YEAR']
            output_df['SPEI'] = out
            output_df.drop(output_df.index[np.arange(0,time-1)],inplace=True)
    # else:
    #     output_df = df.DataFrame()
    #     average_precip = df['precipitation'].mean()
    #     average_aet = df['AET'].mean()
    #     df['precipitation'] = df['precipitation'].fillna(average_precip)
    #     df['AET'] = df['AET'].fillna(average_aet)
    #     output_df = spaei(df['precipitation'],df['AET'])
    if output_csv_path is not None:
        print (output_df.head())
        output_df.to_csv(output_csv_path)
    return output_df
        
def input_time(year,month,time,choice):
    mat = scipy.io.loadmat('../input-data/grid.mat')
    out = np.zeros((121,121))
    grid = mat['grid']
    if choice == "SPI":
        mat1 = scipy.io.loadmat('../input-data/india_rain.mat')
        rain = mat1['monthly_rain']

        for i in range(121):
            for j in range(121):
                if grid[i,j]==1:
                    temp = spi(rain[i,j,:],time,1951,year,year)
                    out[i,j] = temp[month-1]
        
    elif choice == "SPEI":
        mat1 = scipy.io.loadmat('../input-data/india_rain.mat')
        rain = mat1['monthly_rain']
        mat2 = scipy.io.loadmat('../input-data/PET.mat')
        pet = mat2['PET']

        for i in range(121):
            for j in range(121):
                if grid[i,j]==1:
                    temp = spei(rain[i,j,:],pet[i,j,:],time,1951,year,year)
                    out[i,j] = temp[month-1]
    
    