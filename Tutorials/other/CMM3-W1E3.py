#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Created on Mon Sep 25 10:40:11 2023

##@author: ben

import numpy as np
import matplotlib.pyplot as plt

n = 50

x = np.linspace(0, 4*np.pi, 50).tolist()

print(x)

y = []

for i in range(len(x)):
    y.append(np.sin(x[i]))
    
plt.plot(x, y, 'b-')
plt.show()