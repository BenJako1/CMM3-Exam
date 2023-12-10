# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def PI(n):
    s=0
    pibuf = 0
    for i in range(1,n+1):
        s += 1/i**2
        pi = np.sqrt(6*s)
        re = abs(pi-pibuf)/pi
        ae = abs(pi-np.pi)/np.pi
        pibuf = pi
    return pi, re, ae

for i in [10,100,1000]:
    print(f'approximation of pi at n={i} = {PI(i)}')