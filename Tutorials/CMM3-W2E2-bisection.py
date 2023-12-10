#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:05:40 2023

@author: ben
"""

def bisection(f, a, b, error_limit):
    if f(a) * f(b) >= 0:
        return None
    a_n = a # Instantaneous bounds initialised
    b_n = b
    rel_error = error_limit + 1 # Error control variables initialised
    mid_buffer = 0
    while abs(rel_error) > error_limit:
        midpoint = (a_n + b_n)/2    # Midpoint calculated
        f_midpoint = f(midpoint)
        rel_error = abs((midpoint - mid_buffer)/midpoint) * 100     # Error
        mid_buffer = midpoint
        if f(a_n) * f_midpoint < 0:     # If the midpoint and a-bound have different signs, take the b-bound as the new midpoint
            b_n = midpoint
        elif f(b_n) * f_midpoint < 0:   # If the midpoint and b-bound have different signs, take the a-bound as the new midpoint
            a_n = midpoint
        elif  f_midpoint == 0:
            return midpoint
        else:
            return None
    return (a_n + b_n) / 2

f = lambda x: x**2 + 4*x - 12

print(f(-7.5))

print(bisection(f, 0, -10, 0.1))