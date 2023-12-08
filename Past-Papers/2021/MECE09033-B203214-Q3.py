#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:31:38 2023

@author: ben
"""

MAX_ITER = 10000

def func( x ): # deg -> def
    return (x**2 + 5*(x) - 4) # x*2 -> x**2

def Code(a, b): # ; -> : & c -> b
    if func(a) * func(b) >= 0: # >=
        print("You have not assumed correct values of a and b")
        return 0
    c=a
    for i in range(MAX_ITER):
        c = (b * func(b) - a * func(a))/ (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0: # change as to cs
            b=c
        else:
            a=c
    print("The value of root is : " , '%.4f' %c)

Code(-4, 4)

# Secant method

'''
Changes:
    deg -> def
    x*2 -> x**2
    ; -> : & c -> b
    >=
    corrected function
    change as to cs
'''