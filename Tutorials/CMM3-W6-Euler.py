#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:47:44 2023

@author: ben
"""

import matplotlib.pyplot as plt

g = 9.81

c1, c2, c3 = 10, 14, 17
m1, m2, m3 = 70, 60, 40

R = (c1 + c2 + c3) / (m1 + m2 + m3)

v_0 = 5

t = 0
t_end = 30
dt = 0.1

v = v_0
a = 9.81 - v * R

tList = [0]
vList = [v]
aList = [a]
T12List = [m1 * (g - a) - c1 * v]
T23List = [m3 * (a - g) + c3 * v]

while t < t_end:
    a = 9.81 - v * R
    v += a * dt
    
    T_12 = m1 * (g - a) - c1 * v
    T_23 = m3 * (a - g) + c3 * v
    
    t += dt
    
    tList.append(t)
    vList.append(v)
    aList.append(a)
    T12List.append(T_12)
    T23List.append(T_23)
    
plt.plot(tList, vList)
plt.plot(tList, T12List)
plt.plot(tList, T23List)
plt.grid()
plt.show()