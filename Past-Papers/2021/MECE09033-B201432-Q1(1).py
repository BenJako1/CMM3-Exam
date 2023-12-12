#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:32:50 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

a = 12
b = 1500

r = np.roots([1, 2*a, 3*b, a*b, b**2])

print(r)

wr = -0.62301963
wi = 24.03024141

def x(t):
    return 0.1*np.exp(wr*t)*np.cos(wi*t+np.pi/8)

area = integrate.quad(x, 0, 10)[0]

t = np.linspace(0,10,1000)
plt.plot(t, x(t))
plt.xlim(0,10)
plt.grid()

print(1 + area)