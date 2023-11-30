# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random

x_data = np.array([0.  , 0.06666667, 0.13333333, 0.2 ,  0.26666667, 0.33333333,
     0.4 , 0.46666667, 0.53333333, 0.6 ,  0.66666667, 0.73333333,
     0.8 , 0.86666667, 0.93333333, 1.  , ])

y_data = np.array([ 0.00000000e+00,  7.78309056e-01,  1.24040577e+00,  1.24494914e+00,
      8.90566050e-01,  4.33012702e-01,  1.12256994e-01,  4.54336928e-03,
     -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
     -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

def quadraticInterpolation(x, y, interpolationDensity):
    yMaster = []
    xMaster = []
    for i in range(len(x)-2):
        # Fit three points to a parabola
        a, b, c = np.polyfit(x[i:i+3], y[i:i+3], 2)
        f = lambda X: a * X**2 + b * X + c
        # Generate a linspace of values between point bounds
        x_int = np.linspace(x[i], x[i+1], interpolationDensity)
        # Assign values of y from fitted curved to linspace
        y_int = f(x_int)
        # Append to master list
        yMaster.extend(y_int)
        xMaster.extend(x_int)
    
    a, b, c = np.polyfit(x[-3:], y[-3:], 2)
    f = lambda X: a * X**2 + b * X + c
    # Generate a linspace of values between point bounds
    x_int = np.linspace(x[len(x)-2], x[len(x)-1], interpolationDensity)
    # Assign values of y from fitted curved to linspace
    y_int = f(x_int)
    # Append to master list
    yMaster.extend(y_int)
    xMaster.extend(x_int)
    
    return xMaster, yMaster

x, y = quadraticInterpolation(x_data, y_data, 10)
plt.plot(x_data, y_data, 'ko')
plt.plot(x, y, 'b-')
plt.show()