# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:14:32 2016

@author: jpdjeredjian
"""

# generate all combinations of N items
def powerSet(items):
    """First, it iterates through all 2**N possible combinations (possible binary numbers) Second, for each combination of them (represented in its binary form) check for the 1's inside the number and add the corresponding items to the combo list. But how does it do it ? In a very smart way.
    The shift operator >> shifts all digits to the right X times, where X is the number on the right of the >> operator. For example, 8 (which is equal to 1000) >> 1, will shift the 4 digits 1 step to the right to be (0100) which is equal to 4. Even numbers in binary always have 0 as the first digit on the right whereas odd numbers have 1 as the first number on the right. So, 8 (1000) has 0 on the right .. when we shift it right by 1 .. 4(0100) has 0 on the right, 2(0010) has 0 on the right .. 1(0001) has 1 on the right. So, if we check if the number is odd or not, we can know if there is 1 on the right or not.
    Using this idea, the code tries to shift each different combination by numbers from 0 to N, each time it checks if it's odd or not by checking if there's a remainder of 1 (if (i >> j) % 2 == 1) .. if so, then the number of times we shifted the current combination (j in this case) is the original position of the 1 in the combination .. which we can use as an index for the corresponding item we want to take.
    So if the current combination is 1000 (8) and by shifting it 3 times to the right we have 0001 which is odd, we know that 1 in 1000 is the 3rd bit (starting from 0 from the right to the left). if the list of items are [rice, meat, egg, juice] then items[3] is juice.
    So, for each different combination, we use the binary representation of that combination and use the previous method to search for the 1's in the number and add the corresponding items to the list of the items to be taken.
    It's quite long and complex especially for those who never got exposed to binary numbers before .. but this is the trick.
    The solution to the exercise is quite tricky .. I'm not going to post anything about it here but the idea is so similar but is still tricky."""
    
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            #test bit jth of integer i
        
            #Divido el numero, corrido j lugares a la derecha, por mod 3. Si
            # el resultado es 1, significa que esta en la bag1 y lo meto ahi.
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            #Si en cambio, el resultado es 2, significa que esta en bag2
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
            #Si el resultado es 0, no esta en ninguna bolsa y no lo meto en ninguna
            #No puede haber ninguno otro resultado como remainder: recordar que
            #estamos en Trinary system y los numeros son solo 0, 1 y 2
        yield (bag1, bag2)



#Alternative construction of Power Set from Stack Overflow
from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    
    
#Alternativa creada por mi
a = [1,2,3,4,5]

def powerSetJPD(array):
    zero = ()
    print(zero)
    for i in array:
        comb = combinations(array,i)
        for j in comb:
            print(j)