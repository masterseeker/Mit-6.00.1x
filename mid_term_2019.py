#! python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:13:49 2019
@author: Tech
Julian Daniel
:):) from collections import Counter
"""

print(''.join(list(letter for letter in s if letter not in 'aeiouAEIOU')))

return max(n for n in L if L.count(n) % 2) if [n for n in L if L.count(n) % 2] else None

"""
If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""




#def dict_invert(d):
#    '''
#    d: dict
#    Returns an inverted dictionary according to the instructions above
#    '''
#    invertedDict = {key:[] for key in d.values()}
#    for key in invertedDict:
#        for value in d.keys():
#            if d[value] == key:
#                invertedDict[key].append(value)
#    return {k:v.sort() for k, v in zip(invertedDict, invertedDict.values())}
    
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
     # get a dict where the keys are the values of d and the values are an empty list
    iDict = {key:[] for key in d.values()}
    # add values to new dict keys if they were a key for the the new keys in original dict 
    for key in iDict:
        for value in d.keys():
            if d[value] == key:
                iDict[key].append(value)
    #sort the values of iDict which are of type list
    return {k:sorted(v) for k, v in zip(iDict, iDict.values())}

#Problem 9 learnt about the module Counter inside of collections
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    from collections import Counter
    if not L1 and not L2:
        return (None, None, None)
    c = Counter(L1)
    if c != Counter(L2):
        return False
    mostCommon = c.most_common(1)[0][0]
    occurence = c.most_common(1)[0][1]
    elmType = type(mostCommon)
    return (mostCommon, occurence, elmType)
    
    
    
""" Below is the wrong beacause sorted L1 and L2 might not equal even thogh they
are permutations of each other.
"""    
    
#    sortedL1 = sorted(L1,key = lambda x: type(x) == int)
#    sortedL2 = sorted(L2,key = lambda x: type(x) == int)
#    
#    if sortedL1 != sortedL2:
#        return False
#    #answer is the most common element in the list
#    ans = max(set(L1), key = L1.count)
#    return (ans, L1.count(ans), type(ans))   
#
# 
#
#





































