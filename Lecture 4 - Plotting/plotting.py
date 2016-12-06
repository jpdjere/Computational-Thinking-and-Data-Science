#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 01:06:29 2016

@author: jpdjere
"""

import pylab as plt
#plt.plot([1,2,3,4],[1,4,9,16])

xval = []
linear = []
quad = []
cubic = []
exp = []

for i in range(0,30):
    xval.append(i)
    linear.append(i)
    quad.append(i**2)
    cubic.append(i**3)
    exp.append(1.5**i)
    
plt.figure('all')
plt.title('All curves')
plt.xlabel("Data points")
plt.ylabel("All")
plt.plot(xval,linear, label='linear')
plt.plot(xval,quad, label='quadratic')
plt.plot(xval,cubic, label='cubic')
plt.plot(xval,exp, label='exp')
plt.legend(loc='upper-left')

plt.figure('lin')
plt.clf()
#Limit the domains displayed
plt.ylim(0,100)
plt.xlim(0,60)
plt.title("Linear function")
plt.plot(xval,linear)

plt.figure('cubic vs exp')
plt.title('Cubic versus Exponential')
plt.xlabel("Data points")
plt.ylabel("Y")
#Add label and color and line width
plt.plot(xval,cubic,'b', label='cubic', linewidth=2.5)
plt.plot(xval,exp, 'k', label='exponential')
plt.legend(loc='upperleft')

#How to use subplots
plt.figure('subpltos')
plt.clf()
plt.subplot(221)
plt.ylim(0,1000)
plt.plot(xval,linear, label='linear')
plt.ylabel('Linear')
plt.subplot(222)
plt.ylim(0,1000)
plt.plot(xval,quad, label='quadratic')
plt.ylabel('Quadratic')
plt.subplot(223)
plt.ylim(0,1000)
plt.plot(xval,cubic, label='cubic')
plt.ylabel('Cubic')
plt.yscale('log')
plt.subplot(224)
plt.ylim(0,1000)
plt.plot(xval,exp, label='exp')
plt.ylabel('Exp')





