# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:05:59 2023

@author: s2220517
"""
#A
import numpy as np
from scipy.optimize import minimize_scalar
import scipy.integrate as integrate

def res(p):
    return integrate.quad(lambda x: np.sin(x) * np.cos(p*x), 0, np.pi)[1]

fmin = minimize_scalar(res)

print(fmin.x)

# Checking results

import matplotlib.pyplot as plt

x = np.linspace(0,2, 100)
plt.plot(x, [res(i) for i in x], 'b-')
plt.plot(fmin.x, res(fmin.x), 'ko')
plt.show()

#B
def secant(f,a,b,el):
    if f(a) * f(b) > 0:
        print("Bounds do not contain a root.")
        return None
    an = a
    bn = b
    # Check if a and b bound a root
    re = el + 1
    mbuf = 0
    while re > el:
        mn = an - f(an)*(bn-an)/(f(bn)-f(an))
        fmn = f(mn)
        re = abs((mn - mbuf)/mn) * 100
        mbuf = mn
        if f(an) * fmn < 0:
            bn = mn
        elif f(bn) * fmn < 0:
            an = mn
    return an - f(an)*(bn-an)/(f(bn)-f(an))

# we solve equation f(x)=0
f = lambda x: np.sin(x) * np.cos(fmin.x*x)

# first root
solution = secant(f,1.5,2.5,0.001) 
print(solution)

x = np.linspace(0, np.pi, 100)
plt.plot(x, f(x), 'b-')
plt.plot(solution, 0, 'ko')
plt.grid()