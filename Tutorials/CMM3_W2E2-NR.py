#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:54:03 2023

@author: ben
"""

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
f = lambda x: x**3 + 2*x**2 + 1
df = lambda x: 3*x**2 + 4*x

# first root
solution = NewtonRaphson(f,df,1,0.0005) 
print(solution)
