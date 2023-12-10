#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:54:03 2023

@author: ben
"""

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
f = lambda x: x**2 + 4*x - 1

# first root
solution = secant(f,0,-5,0.001) 
print(solution)
