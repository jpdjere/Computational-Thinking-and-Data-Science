# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:41:32 2016

@author: jpdjeredjian
"""

#--------------------------REPITO CODIGO QUE NECESITO-------------#
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
        
    def getCost(self):
        return self.calories
        
    def getDensity(self):
        return self.getValue()/self.getCost()
        
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' +str(self.calories) + '>'
        
def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
    name a list of strings
    values and calories lists of numbers
    returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
    
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost .= 0, keyFunction maps 
    elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
            
    return (result, totalValue)
    
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print('    ', item)
        
def testGreedys(foods, maxUnits):
    print('use greedy by value to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate ',maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.getDensity)
    
#------------------LECTURE 2 --------------------------#
    
def maxVal(toConsider, available):
    """ Assumes toConsider a list of items, asumes available a weight.
    Returns a tuple of the total value of a solution to 0/1 Knapsack problem and
    the items of that solution"""
    if toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        #Explore right branch only
        result = maxVal(toConsider[1:], available)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], available - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], available)
        
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken = ', val)
    if printItems:
        for item in taken:
            print('    ', item)
            
            
#--------------------------REPITO CODIGO QUE NECESITO-------------#
            
import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items
    
#==============================================================================
# for numItems in (5, 10, 15, 20, 25 , 30, 35, 40, 45):
#     items = buildLargeMenu(numItems, 90, 250)
#     testMaxVal(items, 750, False)
#==============================================================================
    
#---------------  Normal recursive Fibonacci Function----- #
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fastFib(n , memo = {}):
    if n == 0 or n == 1:
         return 1
    else:
        try:
            return memo[n]
        except KeyError:
            result = fastFib(n-1, memo) + fastFib(n-2, memo)
            memo[n] = result
            return result
                 
        
#--------------Go back o old maxVal() function and add a memo to it------###
def fastMaxVal(toConsider, available, memo = {}):
    '''Memo is a dictionary, where its key is a tuple 
        (items left to be considererd, avaliable weight). Items left to be conisdered is
        represented by len(toConsider). This works because the items are always removed
        from the front of the list, and if we know how long the remaining list is, we
        know which items remain.
        First thing the function does is check if the optimal choice of items given
        the available weight is already on the demo. Last thing is update the memo.
        Returns a tuple of the total value of a solution to the 0/1 Knapsack problem
        and the subjects of that solution.'''
    if (len(toConsider), available) in memo:
        result = memo[(len(toConsider), available)]
    elif toConsider == [] or available == 0:
        result = (0,())
    elif toConsider[0].getCost() > available:
        #Explore right branch only (left branch is not valid)
        result = fastMaxVal(toConsider[1:], available, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = fastMaxVal(toConsider[1:], available - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], available, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), available)] = result
    return result
        
#-------Reescribo testMaxVal agregando "algorithm" para compar maxVal con testMaxVal        
def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print("Menu contains ", len(foods), " items")
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken = ', val)
    if printItems:
        for item in taken:
            print('    ', item)
            
for numItems in (5, 10, 15, 20, 25 , 30, 35, 40, 45):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, False)