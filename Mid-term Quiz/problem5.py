#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:37:44 2016

@author: jpdjere
"""

def max_contig_sum(L,maxSum = 0):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    cL = L[:]
#    print("\n\nTras el llamado recursivo la lista es: ",cL)
    if L == []:
        return maxSum

    
    for i in range(len(L)+1):
#        print("\nEntro al loop numero :",i)
#        print(cL[:i])
#        print("La suma es: ", sum(cL[:i]))
        if sum(cL[:i]) > maxSum:
            maxSum = sum(cL[:i])
#    print("MaxSum es: ",maxSum)
    return max_contig_sum(L[1:],maxSum)
    
    
def max_contig_sum(L,maxSum = 0):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    cL = L[:]
    if L == []:
        return maxSum
    
    for i in range(len(L)+1):
        if sum(cL[:i]) > maxSum:
            maxSum = sum(cL[:i])

    return max_contig_sum(L[1:],maxSum)