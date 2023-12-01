#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:48:21 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

def Sim(y_0, t_end, dt):
    t = 0
    y = y_0
    yList = [y]
    tList = [0]
    mList = [0]
    ybuf = y
    while t <= t_end:
        y += (10 * y**2-y**3) * dt
        t += dt
        m = (y-ybuf)/dt
        ybuf = y
        print(y)
        mList.append(m)
        tList.append(t)
        yList.append(y)

    print(yList[round(4/dt)], yList[round(5/dt)], yList[round(10/dt)])
    delay = tList[mList.index(max(mList))]
    plt.plot(tList, yList)
    plt.grid()
    plt.show()
    print(delay)
  
Sim(0.02, 10, 0.019)
#for i in [0.02, 0.01, 0.005]:
    #Sim(i, 0, 10, dt)


