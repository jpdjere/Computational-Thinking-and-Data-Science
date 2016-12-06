#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:13:44 2016

@author: jpdjere
"""
    
        
def checkSum(L,mults,s):
    if len(L) == len(mults):
        return sum([i*j for (i, j) in zip(L, mults)]) == s
    else:
        return "Different lengths of lists"
        
        
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    lenL = len(L)
    mults = [0] * lenL    
           
    for i in range(len(mults)): #i es el numero del multiplicador
        if i == 0: #esto hago al evalular el primer multiplicador
            possMult = list(reversed(range(s+1)))  #creo lista de posibles multis
            for j in possMult: #j son los posibles multiplicadores
                mults[i] = j
#                print((L,mults))
                if checkSum(L,mults,s):
                    return sum(mults)
        else:
            possMult = list(reversed(range(s+1)))  #creo lista de posibles multis
            for j in possMult: #j son los posibles multiplicadores
                mults[i-1] = s
                mults[i] = j
#                print((L,mults))
                if checkSum(L,mults,s):
                    return sum(mults)
    
    return 'no solution'

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    lenL = len(L)
    mults = [0] * lenL 
           
    for i in range(len(mults)): #i es el numero del multiplicador
#        print("-------new I--------")
        if i == 0: #esto hago al evalular el primer multiplicador
            possMult = list(reversed(range(s+1)))  #creo lista de posibles multis
            for j in possMult: #j son los posibles multiplicadores
                mults[i] = j
#                print(mults)
                if checkSum(L,mults,s):
                    return sum(mults)
#            print("-------new J--------")
        else:
            possMult = list(reversed(range(s+1)))  #creo lista de posibles multis
            #[11,10,9,8,...,1,0]
            for k in range(s+1):
#                print("-------new K--------")
                for j in possMult: #j son los posibles multiplicadores
#                    print("-------new J--------")
                    mults[i-1] = s-k
                    mults[i] = j
#                    print(mults)
                    if checkSum(L,mults,s):
                        return sum(mults)
#                    print("-------end J--------")
#                print("-------end K--------")
            
            
    
    return 'no solution'
      