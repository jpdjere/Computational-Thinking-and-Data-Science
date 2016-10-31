# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:23:52 2016

@author: jpdjeredjian
"""
from itertools import *
def powerSet(array):
    zero = ()
    print(zero)
    for i in array:
        comb = combinations(array,i)
        for j in comb:
            print(j)
            
            


def powerSet2(items):
    n = len(items)
    ps = []
    for i in range(n+1):
        ps.extend(combinations(items, i))
    return ps