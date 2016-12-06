#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:13:57 2016

@author: jpdjere
"""
import pylab, random

        
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    std = (tot/len(X))**0.5
    return mean, std
    
def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend, weights =
               pylab.array(len(means)*[1])/len(means), hatch = style)
    return getMeanAndStd(means)
    

mean, std = plotMeans(1,1000000,19, '1 die', 'b', 'o')
print('Mean of rolling 1 die = ',str(mean), ',', ' Std = ', std)             
mean, std = plotMeans(50,1000000, 19, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 dice = ',str(mean), ',', ' Std = ', std)
pylab.title('Rolling Continous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()


#==============================================================================
# Now try the same for a roulette
#==============================================================================
import roulette
numTrials = 50000
numSpins = 200
game = roulette.FairRoulette()
                    
means = []
for i in range(numTrials):
    means.append(roulette.findPocketReturn(game,1,numSpins)[0]/numSpins)

pylab.figure('roulette')
pylab.hist(means, bins = 19, weights = pylab.array(len(means)*[1])/len(means))
pylab.xlabel('Mean Return')
pylab.ylabel('Probability')
pylab.title('Expected return Betting a Pocket')