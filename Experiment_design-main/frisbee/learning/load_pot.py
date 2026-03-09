import nidaqmx
from psychopy import visual, core, event
import pandas as pd
import numpy as np 
import function as f

####```This script is for checking to see if the pot is running

### initialize task
timer = core.Clock()
task = nidaqmx.Task() #the with statement automatically closes it 
task.ai_channels.add_ai_voltage_chan("Dev1/ai1", min_val = -5.0, max_val = 5.0) #adds a voltage channel 
task.timing.cfg_samp_clk_timing(1000, sample_mode =nidaqmx.constants.AcquisitionType.CONTINUOUS)
task.start()

time_sec = 5

screen_to_use =1
window = visual.Window(
    fullscr=True,
    monitor="testMonitor",
    units="pix",
    color="white",
    # waitBlanking=False,
    screen=1,
    size=[3440, 1440],
)

cursor = visual.Circle(window, radius = 20, fillColor ='black')
# target = visual.Circle(window, radius = 30, fillColor ='blue',pos=(-860, 0), units='pix')
# target_hit = visual.Circle(window, radius = 40, fillColor ='red',pos=(860, 0), units='pix')
# cal_target = visual.Line(window, start=(-1720, 0), end=(-1715, 0), lineColor='black', lineWidth=2)



timer = core.Clock()

while timer.getTime() < time_sec:
    pot_data=f.get_data(task)
    new_position = f.volt_to_pix(pot_data[-1])
    print(new_position)
    cursor.pos = [new_position, 0] #x and y
    cursor.draw()
    window.flip()






# #looping through conditions
# data = pd.read_csv('trials.csv')

# #loop through the data frame, print off each trial, target, block 
# target_values = []
# for i in range(data.shape[0]):
#     x = data['target'][i]
#     # x *= 2
#     target_values.append(x)
# #load target, multiply by 2, save it as a new csv 
# target_values =pd.DataFrame(target_values)
# print(target_values)

# target_values.to_csv('data/target_x2.csv')




# #data saving

# target.draw()
# win.flip()
# event.waitKeys()
# win.close()
# core.quit()
# with ni.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("Dev1/ai0", min_val=-5.0, max_val=5.0)
#     task.read()



# random_data = [0,4,6,2,5]


# # 3. Create the DataFrame directly from a dictionary
# df_final = pd.DataFrame({
#     'target': target_values,
#     'data': random_data
# })


