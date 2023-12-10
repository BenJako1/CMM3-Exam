# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:41:19 2023

@author: s2220517
"""
import numpy as np
from scipy.optimize import minimize

P = 200000
E = 200000000000
H = 2.75

def sl(x):
    return P/(np.pi * (x[0]/2)**2 - np.pi * (x[0]/2-x[1])**2)

def I(x):
    return (np.pi/4 * ((x[0]/2)**4 - (x[0]/2-x[1])**4))

def sb(x):
    return (np.pi * E * I(x) / (H**2 * x[0] * x[1]))

def cost(x):
    return 0.7 * (7800 * H * (np.pi * (x[0]/2)**2 - np.pi * (x[0]/2-x[1])**2)) + 0.9 * x[0]

print(sb([0.01, 0.001]))

cons = ({'type': 'ineq', 'fun': lambda x:  0.8*sb(x) - sl(x)})

bnds = ((0.01, 0.1), (0.001, 0.01))

res = minimize(cost, np.array([0.05, 0.005]), method='SLSQP', bounds=bnds,
               constraints=cons)

print(res)