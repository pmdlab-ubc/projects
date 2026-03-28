import nidaqmx
import numpy as np
import matplotlib.pyplot as plt

def get_data(task):
    while True:
        data = task.read(
            number_of_samples_per_channel=nidaqmx.constants.READ_ALL_AVAILABLE
        )
        if len(data) == 0:
            continue
        else:
            # print(data)
            return data
#volts to pixels 
def volt_to_pix_old(voltage):
    a = -3442.07
    b =12641.55

    return a*voltage + b
# volt = (p-b)/a

def expo_filt(raw, previous, alpha):
    x = (alpha* raw )+ ((1-alpha) * previous)
    return x

def get_voltage(task):
    while True:
        pot_data =task.read(number_of_samples_per_channel=nidaqmx.constants.READ_ALL_AVAILABLE)
        if len(pot_data) == 0: #the pot is reading in blank 
            continue
        else:
            return(pot_data)
        
def pix_to_deg(pix):
    a = 0.02043189
    b = 108.333333
    return a*pix + b


def get_calibration_coeffs(calibration_voltages, calibration_pixels):
    """
    Input: Lists of recorded voltages and their corresponding pixel targets.
    Output: A list of coefficients [a, b, c, d] for the polynomial equation.
    """
    # Degree 3 is standard for curved monitor geometric distortion
    coeffs = np.polyfit(calibration_voltages, calibration_pixels, 3)
   
    print("-" * 30)
    print("COPY THESE NUMBERS FOR YOUR CONVERSION FUNCTION:")
    print(list(coeffs)) # Prints them as a clean list you can copy
    print("-" * 30)
   
    return coeffs



def volt_to_pix(current_voltage):

    coeffs = [1718.79734603, -10845.96261347, 26018.35762271, -22670.53264086]
   
    # Calculate the pixel value using the polynomial math
    calculated_pixel = np.polyval(coeffs, current_voltage)
   
    # Return as integer 
    return int(calculated_pixel)



