#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:30:39 2023

@author: ben
"""

import numpy as np

def func(x):
    return 1/np.sin(x) + 1/4

def root(guess, tolerance, n):
    x = guess
    xbuf = 0
    for i in range(n):
        x = func(x)
        if abs(x - xbuf) < tolerance:
            return x
        xbuf = x
    raise ValueError(f'Root finding did not converge after {n} iterations')
    
#print(root(1, 0.0001, 1000))

def secant(f,a,b,el):
    if f(a) * f(b) > 0:
        print("Bounds do not contain a root.")
        return None
    an = a
    bn = b
    # Check if a and b bound a root
    re = el + 1
    mbuf = 0
    i =0
    while re > el:
        mn = an - f(an)*(bn-an)/(f(bn)-f(an))
        fmn = f(mn)
        re = abs((mn - mbuf)/mn) * 100
        mbuf = mn
        if f(an) * fmn < 0:
            bn = mn
        elif f(bn) * fmn < 0:
            an = mn
        i += 1
        if i > 1000:
            raise ValueError(f'Root finding did not converge after {i} iterations')
    return an - f(an)*(bn-an)/(f(bn)-f(an))

f = lambda x: x - (1/np.sin(x) + 1/4)

#print(secant(f, 0.0001, 4, 0.001))

def NewtonRaphson(f,df,x0,el):
    xn = x0
    # Check if a and b bound a root
    re = el + 1
    xbuf = 0
    while re > el:
        re = abs((xn - xbuf)/xn) * 100
        xbuf = xn
        fxn = f(xn)
        dfxn = df(xn)
        if round(dfxn, 5) == 0:
            print("Stopped at minimum at:")
            return round(xn,5) , round(fxn, 5)
        xn -= fxn/dfxn
    return xn

# we solve equation f(x)=0
df = lambda x: 1 + (np.sin(x)**(-2)*np.cos(x))

# first root
solution = NewtonRaphson(f,df,2,0.0005) 
print(solution)