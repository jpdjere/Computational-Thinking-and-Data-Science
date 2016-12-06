#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:33:20 2016

@author: jpdjere
"""
import random

def all_same(items):
    return all(x == items[0] for x in items)
    
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    same = 0
    for i in range(numTrials):
        
        bucket = ['r','g']*3
        selected = []
        for i in range(3):
            chosen = random.choice(bucket)
            selected.append(chosen)
            bucket.remove(chosen)
#            print(chosen)
        
        if all_same(bucket):
#            print(True)
            same += 1

            
    return same/numTrials
        

            
        