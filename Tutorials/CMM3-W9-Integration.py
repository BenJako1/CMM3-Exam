#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:29:04 2023

@author: ben
"""

import numpy as np

def func(x):
    return x**2 + 4 * x - 12

def Trapezoid(func, lowLim, highLim, res):
    x = np.linspace(lowLim, highLim, res)
    area = 0
    for i in range(len(x)-1):
        area += func(x[i]) * (x[i+1]-x[i]) + 0.5 * (func(x[i+1])-func(x[i])) * (x[i+1]-x[i])
    area += func(x[-2]) * (x[-1]-x[-2]) + 0.5 * (func(x[-1])-func(x[-2])) * (x[-1]-x[-2])
    return area

def Simpson_Third(func, lowLim, highLim, res):
    x = np.linspace(lowLim, highLim, res)
    area = 0
    for i in range(len(x)-1):
        area += (x[i+1]-x[i])/6 * (func(x[i]) + 4 * func((x[i+1]+x[i])/2) + func(x[i+1]))
    area += (x[-1]-x[-2])/6 * (func(x[-2]) + 4 * func((x[-1]+x[-2])/2) + func(x[-1]))
    return area

def Simpson_3_8ths(func, lowLim, highLim, res):
    x = np.linspace(lowLim, highLim, res)
    area = 0
    for i in range(len(x)-1):
        area += (x[i+1]-x[i])/8 * (func(x[i]) + 3 * func((x[i+1]+2*x[i])/3) + 3 * func((2*x[i+1]+x[i])/3) + func(x[i+1]))
    area += (x[-1]-x[-2])/6 * (func(x[-2]) + 3 * func((x[-1]+2*x[-2])/3) + 3 * func((2*x[-1]+x[-2])/3) + func(x[-1]))
    return area

print(Simpson_3_8ths(func, -10, 10, 1000))

import matplotlib.pyplot as plt

iter_num = [100, 200, 500, 1000, 2500, 5000, 10000]
trap = []
s3 = []
s38 = []
for n in iter_num:
    trap.append(Trapezoid(func, -10, 10, n))
    s3.append(Simpson_Third(func, -10, 10, n))
    s38.append(Simpson_3_8ths(func, -10, 10, n))
plt.plot(iter_num, trap)
plt.plot(iter_num, s3)
plt.plot(iter_num, s38)
plt.show()
