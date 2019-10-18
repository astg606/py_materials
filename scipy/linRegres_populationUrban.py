#!/usr/bin/env python
'''
    We analyze the percentage US urban population since 1790.
    We calculate a linear regression model and plot the data
    
'''

#-------------
# Load modules
#-------------
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def predict_line(x, m, b):
    '''
      Compute: y = mx + b
    '''
    return m*x+b

#--------------
# Read the data
#--------------
fName = 'populationUS.txt'
data = np.genfromtxt(fName, skip_header=6, usecols=(0,4))

x = data[:,0] # Year
y = data[:,1] # Urban percentage

#--------------------------------
# Determine the linear Regression
#--------------------------------
slope, y_intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)

# Calculate some additional outputs
predict_y = predict_line(x, slope, y_intercept)
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

#---------
# Plotting
#---------
bfline = 'y='+"%5.4f"%slope+'x'+"%8.4f"%y_intercept 
plt.plot(x, y, 'o', label='original data')
plt.plot(x, predict_y, 'r-', label='Fitted line: '+bfline)
plt.legend(loc='upper center')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of US Urban Population over Time')
plt.show()
