#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:50:22 2023

@author: ben
"""

import sympy as sp

x, w, T = sp.symbols('x, w, T')

f = sp.Function('f')(x)

expr = sp.Eq(f.diff(x, x), w/T * sp.sqrt(1 + f.diff(x)**2))

sol = sp.dsolve(expr, f)