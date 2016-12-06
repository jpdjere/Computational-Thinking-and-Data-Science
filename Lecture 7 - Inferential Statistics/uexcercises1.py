#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 01:25:33 2016

@author: jpdjere
"""
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    std = (tot/len(X))**0.5
    return mean, std, std/mean

    
def stdDevOfLengths(L):
    tot = 0.0
    
    if len(L) == 0:
        return float('NaN')
    lengths = []
    
    for i in L:
        lengths.append(len(i))
    mean = sum(lengths)/len(lengths)
    for length in lengths:
        tot += (length-mean)**2
    std = (tot/len(lengths))**0.5
    return std