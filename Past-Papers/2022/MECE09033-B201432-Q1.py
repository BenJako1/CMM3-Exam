#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:07:35 2023

@author: ben
"""

import numpy as np

def PI(n):
    s = 0
    pibuf = 0
    for i in range(1, n+1):
        s += 1 / i**2
        pi = np.sqrt(6*s)
        rel = abs(pi-pibuf)/pi
        pibuf = pi
        absolute = abs(pi-np.pi)/np.pi
        
    return pi, rel, absolute
    
for n in [10, 100, 1000]:
    print(f'at n={n}: pi = {PI(n)}')
    

# Q1 completed in 5min 12s