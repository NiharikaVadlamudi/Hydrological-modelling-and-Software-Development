
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import helper_functions
import scipy.stats
import scipy.special 

def _validate_array(
        values: np.ndarray,
        periodicity = "monthly",
) -> np.ndarray:

    periodicity = "monthly"
    if len(values.shape) == 1:

        if periodicity is None:
            message = "1-D input array requires a corresponding periodicity "\
                      "argument, none provided"
            print(message)
            raise ValueError(message)

        elif periodicity == "monthly":
            
            values = helper_functions.reshape_to_2d(values, 12)

        elif periodicity == "daily":
            
            values = helper_functions.reshape_to_2d(values, 366)

        else:
            message = "Unsupported periodicity argument: '{0}'".format(periodicity)
            print(message)
            raise ValueError(message)

    elif (len(values.shape) != 2) or \
            ((values.shape[1] != 12) and (values.shape[1] != 366)):

        
        message = "Invalid input array with shape: {0}".format(values.shape)
        print(message)
        raise ValueError(message)

    return values
def gamma_parameters(
        values: np.ndarray,
        data_start_year: int,
        calibration_start_year: int,
        calibration_end_year: int,
        periodicity = "monthly",
) -> (np.ndarray, np.ndarray):
    

    
    monthly = 12
    daily = 366
    _FITTED_INDEX_VALID_MIN = -3.09
    _FITTED_INDEX_VALID_MAX = 3.09
    if (np.ma.is_masked(values) and values.mask.all()) or np.all(np.isnan(values)):
        if periodicity == "monthly":
            shape = (12,)
        elif periodicity == "daily":
            shape = (366,)
        else:
            raise ValueError("Unsupported periodicity: {periodicity}".format(periodicity=periodicity))
        alphas = np.full(shape=shape, fill_value=np.NaN)
        betas = np.full(shape=shape, fill_value=np.NaN)
        return alphas, betas

    
    values = _validate_array(values, periodicity)

    
    values[values == 0] = np.NaN

    
    data_end_year = data_start_year + values.shape[0]

    
    if (calibration_start_year < data_start_year) or \
            (calibration_end_year > data_end_year):
        calibration_start_year = data_start_year
        calibration_end_year = data_end_year

    
    calibration_begin_index = calibration_start_year - data_start_year
    calibration_end_index = (calibration_end_year - data_start_year) + 1

    
    calibration_values = values[calibration_begin_index:calibration_end_index, :]

    
    means = np.nanmean(calibration_values, axis=0)
    log_means = np.log(means)
    logs = np.log(calibration_values)
    mean_logs = np.nanmean(logs, axis=0)
    a = log_means - mean_logs
    alphas = (1 + np.sqrt(1 + 4 * a / 3)) / (4 * a)
    betas = means / alphas

    return alphas, betas
def transform_fitted_gamma(
        values: np.ndarray,
        data_start_year: int,
        calibration_start_year: int,
        calibration_end_year: int,
        alphas: np.ndarray = None,
        betas: np.ndarray = None,
        periodicity = "monthly"
) -> np.ndarray:
    

    
    if (np.ma.is_masked(values) and values.mask.all()) or np.all(np.isnan(values)):
        return values

    
    values = _validate_array(values, periodicity)

    
    zeros = (values == 0).sum(axis=0)
    probabilities_of_zero = zeros / values.shape[0]

    
    values[values == 0] = np.NaN

    
    if (alphas is None) or (betas is None):
        alphas, betas = \
            gamma_parameters(
                values,
                data_start_year,
                calibration_start_year,
                calibration_end_year,
                periodicity,
            )

    
    gamma_probabilities = scipy.stats.gamma.cdf(values, a=alphas, scale=betas)

    
    probabilities = probabilities_of_zero + \
                    ((1 - probabilities_of_zero) * gamma_probabilities)

    
    
    
    return scipy.stats.norm.ppf(probabilities)
