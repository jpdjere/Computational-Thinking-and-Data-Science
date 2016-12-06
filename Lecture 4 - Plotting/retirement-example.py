#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 00:21:31 2016

@author: jpdjere
"""

#EXAMPLE: Planning for retirement
import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings
    
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+str(monthly))
        plt.legend(loc = 'upper left')
        
displayRetireWMonthlies([500,600,700,800,900,1000,1100], .05, 40*12)

def displayRetireWRate(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+str(month)+ ': ' + str(int(rate*100)) + '%')
        plt.legend(loc = 'upper left')
        
displayRetireWRate(800,[0.03, 0.05, 0.07], 40*12)

#Junto Months and rates
def displayRetireWMonthsandRates(monthlies, rates, terms):
    plt.figure('reitreBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot( xvals, yvals, label = 'retire: ' +str(monthly)+ ": " + str(int(rate*100))+ "%")
            plt.legend(loc = 'upper left')

displayRetireWMonthsandRates([500,700,900,1100],[0.03, 0.05,0.07], 40*12)


#Como el grafico es un quilombo, intento arreglarlo ocn labels
def displayRetireWMonthsandRates(monthlies, rates, terms):
    plt.figure('reitreBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel, label = 'retire: ' +str(monthly)+ ": " + str(int(rate*100))+ "%")
            plt.legend(loc = 'upper left')
            
displayRetireWMonthsandRates([500,700,900,1100],[0.03, 0.05,0.07], 40*12)      