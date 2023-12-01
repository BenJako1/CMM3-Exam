#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:26:20 2023

@author: ben
"""

# Q1a
import numpy as np

def PI(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i**2
    return np.sqrt(6*s)

print(PI(10))

#------------------------------------------------------------------------------

def PI_Rel(error_limit):
    s = 0
    re = error_limit + 1
    xbuf = 0
    i = 1
    while re > error_limit:
        s += 1/i**2
        x = np.sqrt(6*s)
        re = abs((x - xbuf)/x) * 100
        xbuf = x
        i += 1
    return x

#print(PI_Rel(0.0000000001))

#------------------------------------------------------------------------------

#Q1b
def PI_2(n):
    s = 0
    re = 0
    xbuf = 0
    for i in range(1,n+1):
        s += 1/i**2
        x = np.sqrt(6*s)
        re = abs((x - xbuf)/x) * 100
        xbuf = x
    print(f'relative error (n={n})= {re}')
    print(f'absolute error (n={n})= {abs(np.pi-x)/np.pi}')
    print(f'pi approximation (n={n}): {x}')
    return x


for i in [10, 100, 1000]:
    PI_2(i)