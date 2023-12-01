#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:13:22 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

A0 = 0.1
b = 0.1
m = 1
w = 31.42 # 5 in rad/s

def x(t):
    return (A0 * np.exp(-b/(2*m)*t)*np.cos(0*t))
t = 0
while x(t) > A0/100:
    t += 0.1
print(t)
tList = np.linspace(0, t, 100)
plt.plot(tList, x(tList))
t0 = t
while x(t0/2) > A0/100:
    b += 0.0001

print(b)

tList = np.linspace(0, t, 100)
plt.plot(tList, x(tList))
plt.plot(tList, [A0/100 for i in tList], 'k--')
plt.ylim([0,0.01])