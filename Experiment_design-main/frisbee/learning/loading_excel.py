import pandas as pd
import numpy as np 


### this script is a basic for loop for running through a csv file
data = pd.read_csv('trials.csv')
print(data.shape)

#loop through the data frame, print off each trial, target, block 
target_values = []
for i in range(data.shape[0]): #go down each row
    x = data['target'][i] #go down the target column
    # x *= 2
    target_values.append(x)


#load target, multiply by 2, save it as a new csv 
target_values =pd.DataFrame(target_values)
print(target_values)
print(data.shape)

# target_values.to_csv('data/target_x2.csv')

