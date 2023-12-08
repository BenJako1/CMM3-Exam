#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:36:40 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

t = 0
h = 1
dt = 0.01

s = 0.1
r0 = 0.5
h0 = r0/s

A = 0.01
g = 9.81

tList = [t]
hList = [h]

V0 = 1/3 * np.pi * h0**2 * s
V = 1/3 * np.pi * h * s * (h+h0) - V0

while h > 0:
    flowrate = A * np.sqrt(2 * g * h)
    V -= flowrate * dt
    h = np.roots([np.pi/3*s, np.pi/3*s*h0 , -V])
    print(h)
    break
    print(h)
    
    t += dt
    
    hList.append(h)
    tList.append(t)
    
plt.plot(tList, hList)