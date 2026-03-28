###
from psychopy import visual, core
import numpy as np

'''
This is calibration check for voltage to pix. this code displays a visual stimulus for each pixel
'''

win = visual.Window(
    size=(3440, 1440),
    fullscr=True, 
    units='pix',
    color=[-1, -1, -1] # Black background
)

# 2. Get the actual width and height of the window in pixels
WIDTH, HEIGHT = win.size

# 3. Create a texture array
# PsychoPy uses colors on a scale from -1.0 to 1.0 by default.
# We make an array that is 1 row tall, WIDTH columns wide, with 3 color channels (RGB).
texture = np.empty((1, WIDTH, 3), dtype=np.float32)

# PsychoPy Color scale: 
# Red    =[ 1.0, -1.0, -1.0]
# Yellow =[ 1.0,  1.0, -1.0]

# Set every even pixel (0, 2, 4...) to Red
texture[0, 0::2, :] = [1.0, -1.0, -1.0]

# Set every odd pixel (1, 3, 5...) to Yellow
texture[0, 1::2, :] = [1.0, 1.0, -1.0]

# 4. Create an ImageStim from the texture #this creates a image
# size=(WIDTH, HEIGHT) stretches our 1-pixel high pattern down the whole screen
# interpolate=False is CRUCIAL: it ensures the colors stay sharp 1-pixel lines and don't blur into orange
lines_stim = visual.ImageStim(
    win=win,
    image=texture,
    size=(WIDTH, HEIGHT),
    interpolate=False 
)


lines_stim.draw()
win.flip()
core.wait(5.0)
win.close()
core.quit()
