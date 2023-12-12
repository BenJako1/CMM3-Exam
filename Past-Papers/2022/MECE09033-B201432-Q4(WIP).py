#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:44:15 2023

@author: ben
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t, m, b, k = sp.symbols('t, m, b, k')
x = sp.Function('x')(t)
EQ1 = sp.Eq(m*x.diff(t,t) + b*x.diff(t) + k*x, 0)
sol = sp.dsolve(EQ1)
#sp.pprint(sol)

A0 = 1
m = 1
b = 0.1
omega = 31.42 # in rad/sec

def x(t, b):
    return A0*sp.exp(-b*t/(2*m))*np.cos(omega*t)

def test(tmax, b):
    t = 0
    dt = 0.01
    v = []
    peak = []
    while t < tmax:
        v.append(x(t, b))
        if len(v) > 3:
            if v[-1] < v[-2] and v[-3] < v[-2]:
                peak.append(t)
                if x(peak[-1], b) < A0/100:
                    return peak[-1]
        t += dt
    return None

def half (b):
    t1 = test(100, b)
    t0 = t1
    while t0 > t1/2:
        b += 0.001
        t0 = test(100, b)
        print(t0)
    return b

print(test(100, b))
print(half(b))

# Works but super slow
    