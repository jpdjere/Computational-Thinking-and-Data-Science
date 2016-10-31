# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:22:12 2016

@author: jpdjeredjian
"""

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

    
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95,100,90, 79,50, 10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names,values,calories)
testGreedys(foods, 1000)
print('    ')
testMaxVal(foods, 1000)







    