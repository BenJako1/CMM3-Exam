#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:58:00 2023

@author: ben
"""

import sympy as sym
from scipy.optimize import fsolve

TA, w, x, y0 = sym.symbols('TA, w, x, y0')

y = TA/w*sym.cosh(w/TA*x) + y0 - TA/w

dydx = y.diff(x)
dydx2 = dydx.diff(x)
sym.pprint(dydx2)
dydx2 = dydx2.subs(sym.cosh(w*x/TA), sym.sqrt(1+dydx**2))
sym.pprint(dydx2)
sym.pprint(dydx)

EQ = TA/w*sym.cosh(w/TA*x) + y0 - TA/w - 15
sym.pprint(EQ)
EQ = EQ.subs(x, 50).subs(y0, 5).subs(w, 10)
f = sym.lambdify(TA, EQ)
sol = fsolve(f, [10])
print(sol)