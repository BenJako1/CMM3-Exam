#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:57:35 2023

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

n = 6
A = 25500
P = 115000

def func(i):
    return (((1+i)**n-1)/(i*(1+i)**n))

def interest(tolerance, n):
    for i in np.linspace(0.01, 0.2, n):
        if func(i) <= (P/A + tolerance) and (func(i) >= P/A - tolerance):
            print(P/A, func(i))
            return i
    print("not able to calculate interest.")
    return None

a = interest(0.01, 1000)

x = np.linspace(0.0001, 0.5, 10000)
plt.plot(x, func(x))
plt.plot(x, [P/A for i in x])
plt.plot(a, func(a), 'ko')
plt.grid()

print(f'Interest rate = {a}')

# Question 3 in 18min 29sec