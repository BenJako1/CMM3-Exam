#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:17:12 2023

@author: ben
"""

import numpy as np

t = 0
t_end = 30
dt = 0.001

m0 = 160000
u = 1800
q = 2500
g = 9.81

h = 0

tList = [t]
hList = [h]

while t < t_end:
    v = u * np.log(m0/(m0-q*t)) - g * dt
    h += v * dt
    
    t += dt
    t = round(t, int(-np.log10(dt)))
    
    tList.append(t)
    hList.append(h)

print(f'distance travelled (m) at t={t_end}s = {hList[-1]}')

# Q4 in 5min 53sec