
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import helper_functions
import gamma_transform

def spei(
        precips_mm: np.ndarray,
        pet_mm: np.ndarray,
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
    if (np.ma.is_masked(precips_mm) and precips_mm.mask.all()) \
            or np.all(np.isnan(precips_mm)):
        return precips_mm
    
    if precips_mm.size != pet_mm.size:
        message = "Incompatible precipitation and PET arrays"
        print(message)
        raise ValueError(message)

    
    if np.amin(precips_mm) < 0.0:
        print("Input contains negative values -- all negatives clipped to zero")
        precips_mm = np.clip(precips_mm, a_min=0.0, a_max=None)

    
    p_minus_pet = (precips_mm - pet_mm) + 1000.0

    
    original_length = precips_mm.size

    
    scaled_values = helper_functions.sum_to_scale(p_minus_pet, scale)

    if distribution is "gamma":

        
        if fitting_params is not None:
            alphas = fitting_params["alphas"]
            betas = fitting_params["betas"]
        else:
            alphas = None
            betas = None

        transformed_fitted_values = \
            gamma_transform.transform_fitted_gamma(
                scaled_values,
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

    
    values = \
        np.clip(transformed_fitted_values,
                _FITTED_INDEX_VALID_MIN,
                _FITTED_INDEX_VALID_MAX).flatten()


    return values[0:original_length]

def spei_index(spei_value):
    string_return = ""
    if spei_value >= 2.0:
        string_return = "Extreme wet"
    elif spei_value >=1.5 and spei_value < 2.0:
        string_return = "Severe wet"
    elif spei_value >= 1.0 and spei_value < 1.5:
        string_return = "Moderate wet"
    elif spei_value >= -1.0 and spei_value <1:
        string_return = "Normal"
    elif spei_value >= -1.5 and spei_value < -1:
        string_return = "Moderate dry"
    elif spei_value >= -2.0 and spei_value < -1.5:
        string_return = "Severe dry"
    elif spei_value <= -2.0:
        string_return = "Extreme dry"
    return string_return
if __name__ == '__main__':
    
    df_precip = helper_functions.preprocess_csv('../data/Balehonnur_discharge.csv')
    # df_pet = 
    # values = spei(df_precip, df_pet, 12, 1995, 1995, 2017)
    # print (values[255])
    # print (spei_index(values[255]))
    # plt.plot(values)
