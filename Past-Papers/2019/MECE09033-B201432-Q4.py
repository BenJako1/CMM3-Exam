# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:54:45 2023

@author: s2220517
"""
import numpy as np
import matplotlib.pyplot as plt

R = [6728, 6870, 6728, 6615, 6728]
theta = np.deg2rad([-180, -30, 0, 30, 180])
# Appropriate values
C = 6728
e = 0.035
a = 0

def Rf(i):
    return C/(1+e*np.sin(i+a))

x = np.linspace(-np.pi, np.pi, 360)

plt.plot(x, Rf(x), 'b-')
plt.plot(theta, R, 'ko')

coeff = np.polyfit(theta, R, 4)

def fit(x):
    return coeff[0] * x**4 + coeff[1] * x**3 + coeff[2] * x**2 + coeff[3] * x + coeff[4]

plt.plot(x, fit(x), 'r-')

print(min(fit(x)))