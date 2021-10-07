
import numpy as np
import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt
import helper_functions
import gamma_transform
def spi(
        values: np.ndarray,
        scale: int,
        data_start_year: int,
        calibration_year_initial: int,
        calibration_year_final: int,
        periodicity = "monthly",
        fitting_params = None,
        distribution = "gamma",
        monthly = 1
) -> np.ndarray:


    
    _FITTED_INDEX_VALID_MIN = -3.09
    _FITTED_INDEX_VALID_MAX = 3.09
    shape = values.shape
    if len(shape) == 2:
        values = values.flatten()
    elif len(shape) != 1:
        message = "Invalid shape of input array: {shape}".format(shape=shape) + \
                  " -- only 1-D and 2-D arrays are supported"
        
        raise ValueError(message)

    
    if (np.ma.is_masked(values) and values.mask.all()) or np.all(np.isnan(values)):
        return values

    
    if np.amin(values) < 0.0:
        print("Input contains negative values -- all negatives clipped to zero")
        values = np.clip(values, a_min=0.0, a_max=None)

    
    original_length = values.size

    
    values = helper_functions.sum_to_scale(values, scale)

    
    if periodicity is "monthly":

        values = helper_functions.reshape_to_2d(values, 12)

    elif periodicity is "daily":

        values = helper_functions.reshape_to_2d(values, 366)

    else:

        raise ValueError("Invalid periodicity argument: %s" % periodicity)

    if distribution is "gamma":

        
        if fitting_params is not None:
            alphas = fitting_params["alpha"]
            betas = fitting_params["beta"]
        else:
            alphas = None
            betas = None

        
        values = gamma_transform.transform_fitted_gamma(
            values,
            data_start_year,
            calibration_year_initial,
            calibration_year_final,
            periodicity,
            alphas,
            betas,
        )
    

    else:

        message = "Unsupported distribution argument: " + \
                  "{dist}".format(dist=distribution)
        print(message)
        raise ValueError(message)

    # clip values to within the valid range, reshape the array back to 1-D
    values = np.clip(values, _FITTED_INDEX_VALID_MIN, _FITTED_INDEX_VALID_MAX).flatten()

    # return the original size array
    return values[0:original_length]

def spi_index (spi_value):
    string_return = ""
    if spi_value >= 2.0:
        string_return = "Extremely wet"
    elif spi_value >=1.5 and spi_value < 2.0:
        string_return = "Very wet"
    elif spi_value >= 1.0 and spi_value < 1.5:
        string_return = "Moderate wet"
    elif spi_value >= -1.0 and spi_value <1:
        string_return = "Normal"
    elif spi_value >= -1.5 and spi_value < -1:
        string_return = "Moderate drought"
    elif spi_value >= -2.0 and spi_value < -1.5:
        string_return = "Severe drought"
    elif spi_value <= -2.0:
        string_return = "Extreme drought"
    return string_return 

        
if __name__ == '__main__':
    
    df_precip = helper_functions.preprocess_csv('../data/Balehonnur_discharge.csv')
    values = spi(df_precip, 12, 1995, 1995, 2017)
    print (values[255])
    print (spi_index(values[255]))
    plt.plot(values)
    plt.show()
