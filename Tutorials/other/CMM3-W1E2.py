#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:29:36 2023

@author: ben
"""

import random

length = 20
x = []
index = []


for i in range(length):
    x.append(0)
    
for i in range(length):
    x[i] = random.randint(0,10)
    
print(x)

for i in range(length):
    if x[i] >= 5 and x[i] <= 6: # Differs from instruction but instruction would result in an empty index list
        index.append(i)

print(index)
        