
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def preprocess_csv(dataset, period = "monthly"):
    '''
    Regional calculation

    Parameters
    ----------
    dataset : csv file path
        DESCRIPTION.

    Returns
    -------
    data frame

    '''
    data_frame = pd.read_csv(dataset, index_col = 0, parse_dates = True, squeeze = True)
    data_frame['Date'] = pd.to_datetime(data_frame[['Year', 'Month', 'Day']],errors='coerce')
    data_frame = data_frame.set_index(data_frame["Date"])
    for date, item in zip(data_frame["Date"], data_frame["Item"]):
        if item == 'nan':
            data_frame["Item"] = 0
        if date == "nan":
            data_frame["Date"] = 0
    data_frame_item = data_frame["Item"]
    data_frame_item = data_frame_item.resample('M').mean()
    return data_frame_item
        
def sum_to_scale(
        values: np.ndarray,
        scale: int,
) -> np.ndarray:
    

    
    if scale == 1:
        return values

    sliding_sums = np.convolve(values, np.ones(scale), mode="same")

    
    return np.hstack(([np.NaN] * (scale - 1), sliding_sums))

def reshape_to_2d(
        values: np.ndarray,
        second_axis_length: int,
) -> np.ndarray:
    

    
    shape = values.shape
    if len(shape) == 2:
        if shape[1] == second_axis_length:
            
            return values
        else:
            message = "Values array has an invalid shape (2-D but second " + \
                      "dimension not {dim}".format(dim=second_axis_length) + \
                      "): {shape}".format(shape=shape)
            print(message)
            raise ValueError(message)

    
    elif len(shape) != 1:
        message = "Values array has an invalid shape (not 1-D " + \
                  "or 2-D): {shape}".format(shape=shape)
        print(message)
        raise ValueError(message)

    
    final_year_values = shape[0] % second_axis_length
    if final_year_values > 0:
        pads = second_axis_length - final_year_values
        values = np.pad(values,
                        pad_width=(0, pads),
                        mode="constant",
                        constant_values=np.NaN)

    
    first_axis_length = int(values.shape[0] / second_axis_length)

    
    return np.reshape(values, newshape=(first_axis_length, second_axis_length))



