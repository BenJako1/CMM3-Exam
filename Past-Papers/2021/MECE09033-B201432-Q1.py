#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:10:52 2023

@author: ben
"""

import numpy as np
from scipy.integrate import quad

a = 12
b = 1500

def func(x):
    return (x**4 + 2*a*x**3 + 3*b*x**2 + a*b*x + b**2)

coefficients = [1, 2*a, 3*b, a*b, b**2]

roots = np.roots(coefficients)

print("Roots:", roots)

def disp(t):
    return (0.1*np.exp(-0.62301963*t)*np.cos(24.03024141*t + np.pi/8))

I = quad(disp, 0, 10)

print(I)
