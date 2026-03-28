import nidaqmx
from psychopy import visual, core, event
import pandas as pd
import numpy as np 
import function as f


'''
This script calibrates the voltage from a pot and gives coeff used for converting votlage to pixels
'''
### initialize task

# task = nidaqmx.Task() #the with statement automatically closes it 
# task.ai_channels.add_ai_voltage_chan("Dev1/ai1", min_val = -5.0, max_val = 5.0) #adds a voltage channel 
# task.timing.cfg_samp_clk_timing(1000, sample_mode =nidaqmx.constants.AcquisitionType.CONTINUOUS)
# task.start()



# screen_to_use =1
# window = visual.Window(
#     fullscr=True,
#     monitor="testMonitor",
#     units="pix",
#     color="white",
#     # waitBlanking=False,
#     screen=1,
#     size=[3440, 1440],
# )

# ###### Each line corresponds to a different target position, so you can use this to calibrate the voltage to pixel conversion.
# # line = visual.line.Line(window, start =(-1720,-1720), end=(-1720,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(-1290,-1720), end=(-1290,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(-860,-1720), end=(-860,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(-430,-1720), end=(-430,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(0,-1720), end=(0,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(430,-1720), end=(430,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(860,-1720), end=(860,1720), lineColor ='black',lineWidth = 40) #line for calibration
# # line = visual.line.Line(window, start =(1290,-1720), end=(1290,1720), lineColor ='black',lineWidth = 40) #line for calibration
# line = visual.line.Line(window, start =(1720,-1720), end=(1720,1720), lineColor ='black',lineWidth = 40) #line for calibration

# line.draw()
# window.flip()
# event.waitKeys()

# time_sec = 5
# timer = core.Clock()
# voltage = []
# while timer.getTime() < time_sec:
#     pot_data=f.get_data(task)
#     voltage.append(pot_data)

# #take the mean of the last 5 voltage readings to get a stable estimate of the voltage for that target position. Do this for each target position to get your calibration data.  
# final_5_mean = np.mean(voltage[-5:])
# print(final_5_mean
#       )

# #change calibration voltage and pixel values to your actual data, then run this function to get the coefficients for your conversion function. Paste those coefficients into the volt_to_pix function above.
# # calibration_v = [1.510259897133801,1.395740280818427, 1.245711205533007,1.1027711329457817,0.9655022625171114,0.8282333920884412,0.6849710921058432,0.5594957443478051,0.4008309748664033]
# # pixels = [-1720, -1290, -860, -430, 0, 430, 860, 1290, 1720]
# # coeff = f.get_calibration_coeffs(calibration_v, pixels)
# # print(coeff)

calibration_v = [1.6098926077829674,1.7147454022371675,1.8216604520217516,1.9547403663105798,2.0807312779012137,2.217097911622841,2.3417354681529106,2.462828523333883,2.5656190624576993]
pixels = [-1720, -1290, -860, -430, 0, 430, 860, 1290, 1720]
coeff = f.get_calibration_coeffs(calibration_v, pixels)
print(coeff)
