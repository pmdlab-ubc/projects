import nidaqmx
from psychopy import visual, core, event
import pandas as pd
import numpy as np 
import function as f

####```This script is for making a targeting movment and recording endpoint position

#set variables
time_sec = 5

### initialize task
timer = core.Clock()
task = nidaqmx.Task() #the with statement automatically closes it 
task.ai_channels.add_ai_voltage_chan("Dev1/ai1", min_val = -5.0, max_val = 5.0) #adds a voltage channel 
task.timing.cfg_samp_clk_timing(1000, sample_mode =nidaqmx.constants.AcquisitionType.CONTINUOUS)
task.start()

### create window and cursor
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
target = visual.Circle(window, radius = 30, fillColor='red', pos=(860,0), units='pix')


#empty position list
datapoint = []
time_hit=[]
current =  [f.volt_to_pix(f.get_voltage(task)[-1])]
globalclock = core.Clock()
globalclock.reset()

target_hit_detected = False
while globalclock.getTime() < time_sec:
    prev_pos = current[0]
    pot_data =f.get_voltage(task)
    # print(pot_data)
    new_position = f.volt_to_pix(pot_data[-1]) #takes last voltage reading
    current = [f.expo_filt(new_position,current[0], 0.1)]
    cursor.pos= [current[0],0]
    cursor.draw()
    target.draw()
    window.flip()

    if not target_hit_detected and target.contains(cursor.pos):
        hit_pos = cursor.pos
        hit_time = globalclock.getTime()
        target_hit_detected =True
        target.opacity = 0
        cursor.opacity = 0
        datapoint.append(hit_pos[0])
        time_hit.append(hit_time)
print(datapoint,time_hit)



