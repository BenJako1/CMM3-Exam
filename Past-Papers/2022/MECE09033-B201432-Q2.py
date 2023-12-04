#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:14:09 2023

@author: ben
"""
import matplotlib.pyplot as plt
import numpy as np


t = 0
t_end = 10
dt = 0.01

y = 0.02

yList = [y]
tList = [t]
mList = [0]
ybuf = y

while t < t_end:
    y += (10 * y**2 - y**3) * dt
    t += dt
    
    mList.append((y-ybuf)/dt)
    yList.append(y)
    tList.append(t)
    ybuf = y
    
tList = [round(i,3) for i in tList]
plt.plot(tList, yList)
print(f'at t=4, y {yList[tList.index(4)]}')
print(f'at t=5, y {yList[tList.index(5)]}')
print(f'at t=10, y {yList[tList.index(10)]}')
print(f'delay = {tList[mList.index(max(mList))]}')

# Limit for h (dt) is around 0.02

# Q2 done in 15min 48s