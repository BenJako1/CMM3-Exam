# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:40:50 2023

@author: s2220517
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

c = 1

func = lambda b: np.cosh(b) * np.cos(b) + 1
x = np.linspace(-2,2, 100)
plt.plot(x, func(x))
r = optimize.root(func, [-1, 1])
print(r.x)

f = [np.sqrt(i**4 * c / (2* np.pi)**2) for i in r.x]

print(f)