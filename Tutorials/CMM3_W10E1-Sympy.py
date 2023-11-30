#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:58:03 2023

@author: ben
"""

import sympy as sym

a = 2
b = 5
c = 2

x = sym.Symbol('x')
y = sym.Symbol('y')

dydx = sym.Symbol('dydx')

y = a * sym.sin(b*x + c)

dydx = sym.diff(y, x)

print('function of x: ', y)
print('derivative of f(x): ', dydx)

dydx2 = sym.diff(dydx, x)

print('second derivative of f(x): ', dydx2)

z = sym.Symbol('z')
z = dydx + dydx2

print('z(x) = ', z)

s = sym.Symbol('s')
s = (1/y) * dydx
print('s simplified: ', sym.simplify(s))
print('Taylor expansion of s: ', sym.series(s, n=4))