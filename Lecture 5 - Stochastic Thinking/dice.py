#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 00:18:12 2016

@author: jpdjere
"""

import random
#random.seed(0)

def rollDie():
    return random.choice([1,2,3,4,5,6])
    
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability = ', round(1/(6**len(goal)),8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability = ', round(estProbability,8))   
    
runSim('11111',10000)

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars
    
print('Frequency of double 6 = ', str(fracBoxCars(100000)*100) + '%')