#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:38:29 2023

@author: ben
"""

# -----------------------------------------------------------
# Approximate pi to given acceptable approximate error

import math

errorLimit = 0.0000001

trueValue = math.pi

def pi_approx():
    i = 1
    sm = 0
    pa = 0
    approx = 0
    approxError = 1
    while approxError >= errorLimit:
        sm += 1 / (i)**2
        approx = math.sqrt(6 * sm)
        approxError = abs((approx - pa)/ approx)
        print(approx, approxError)
        pa = approx
        i += 1
    return approx

# -----------------------------------------------------------


# -----------------------------------------------------------
# Main program
     
print(pi_approx())