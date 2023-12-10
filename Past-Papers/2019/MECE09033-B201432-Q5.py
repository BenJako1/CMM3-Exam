# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:16:42 2023

@author: s2220517
"""

from scipy.optimize import minimize, rosen, rosen_der
import numpy as np

w1 = 20000
w2 = 30000
l1 = 1.2
l2 = 1.5
l3 = 1.
B = 3.5
H = 0

def V(theta):
    return (-w1*l1*np.sin(theta[0])-w2*(l1*np.sin(theta[0])+l2*np.sin(theta[1])))

cons = ({'type': 'eq', 'fun': lambda x:  l1*np.cos(x[0])+l2*np.cos(x[1])+l3*np.cos(x[2])-B},
        {'type': 'eq', 'fun': lambda x:  l1*np.sin(x[0])+l2*np.sin(x[1])+l3*np.sin(x[2])-H})

res = minimize(V, np.array([0, 0, 0]), method='SLSQP',constraints=cons)

for i in [0,1,2]:
    print(f'theta {i+1} = {round(res.x[i], 5)} rad')