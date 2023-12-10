#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:17:46 2023

@author: ben
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (y * (1 - y))

y_0 = 0.0179862
x = 0
dx = 0.01
x_end = 10

y = y_0

xList = [x]
yList = [y]

while x < x_end:
    y += f(x, y) * dx
    x += dx
    
    xList.append(x)
    yList.append(y)
    
plt.plot(xList, yList, 'b-')
plt.show()