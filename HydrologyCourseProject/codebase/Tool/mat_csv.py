import scipy.io
import pandas as pd
import numpy as np
mat = scipy.io.loadmat('../input-data/PET.mat')
mat1 = scipy.io.loadmat('../input-data/india_rain.mat')
mat2 = scipy.io.loadmat('../input-data/AET.mat')
pet = mat['PET']
rain = mat1['monthly_rain']
aet = mat2['AET']
rain = rain[61,61,53*12:53*12+7*12]
aet = aet[61,61,24*12:24*12+7*12]
pet = pet[61,61,24*12:24*12+7*12]
years = np.arange(2004,2011)
years = np.repeat(years,12)

data = pd.DataFrame()
data['precipitation'] = rain
data['AET'] = aet
data['PET'] = pet
data['YEAR'] = years
data.to_csv("../input-data/sample_input.csv")