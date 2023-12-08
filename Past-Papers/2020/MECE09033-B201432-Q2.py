#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:30:19 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 9.81

intitialTheta = np.pi/8

t = 0
t_end = 30
dt = 0.001

theta = intitialTheta
av = 0

tList = [t]
avList = [av]
thetaList = [theta]

while t <= t_end:
    av += -g/l * np.sin(theta) * dt
    theta += av * dt
    
    t += dt
    t = round(t, int(-np.log10(dt)))
    
    tList.append(t)
    avList.append(av)
    thetaList.append(theta)

print("NON-LINEARIZED")
for i in [10, 20, 30]:
    print(f' at t = {i}s:\nangular velocity = {avList[tList.index(i)]}\ntheta = {thetaList[tList.index(10)]}')
T = tList[thetaList.index(max(thetaList[round(5/dt):round(10/dt)]))]
print(T)

t = 0
t_end = 30
dt = 0.001

theta = intitialTheta
av = 0

tList1 = [t]
avList1 = [av]
thetaList1 = [theta]

while t <= t_end:
    av += -g/l * theta * dt
    theta += av * dt
    
    t += dt
    t = round(t, int(-np.log10(dt)))
    
    tList1.append(t)
    avList1.append(av)
    thetaList1.append(theta)

print("LINEARIZED")
for i in [10, 20, 30]:
    print(f' at t = {i}s:\nangular velocity = {avList[tList.index(i)]}\ntheta = {thetaList[tList.index(10)]}')

T1 = tList1[thetaList1.index(max(thetaList1[round(5/dt):round(10/dt)]))]
print(T1)

plt.plot(tList, thetaList, 'b-')
plt.plot(tList1, thetaList1, 'r-')
plt.plot(T, max(thetaList[round(5/dt):round(10/dt)]), 'bo')
plt.plot(T1, max(thetaList1[round(5/dt):round(10/dt)]), 'ro')
plt.grid()
plt.show()

print(abs(T-T1)/T*100)

# Question 2 done in 27min 2sec


