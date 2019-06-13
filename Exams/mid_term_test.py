# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:59:09 2018

@author: Tech
"""

"""    problem 3   """""
     
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = lower = 0 
    while base ** exponent < num:
        lower = base ** exponent 
        exponent += 1
    
    higher = base ** exponent
    
    if abs(num - lower) <= abs(higher - num): 
        return exponent - 1 
    else: 
        return exponent
    
    
    
    
""" problem 4 """

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    
    '''
#    listC = []
#    for i in range(len(listA)):
#        listC.append(listA[i] * listB[i])
#    return sum(listC)


    return sum([listA[i] * listB[i] for i in range(len(listA))])

""" problem 5 """

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    ''' 

    return sorted([key for key in aDict if aDict[key] == target])         
        
""" problem 6 """

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1 
        else:
            return helpLaceStrings(s1[1:], s2[1:] , out + s1[0]+ s2[0])
    return helpLaceStrings(s1, s2, '')

""" problem 7 """


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    remove = [i for i in L if not f(i)]

    for i in remove:
        L.remove(i)
    return len(L)

    """ problem 7 smarter solutions"""
    
    """ 1: go backwards so your positon in the loop is not affected by making the 
    shorter if removing elements """
    
    for i in range((len(L)-1, -1, -1)):
        if not f(i):
            L.pop(i)
    return len(L)
    
    """ 2: use slicing so that when you slice the list the global lik is
    not broken
    SO IF YOU APPLY SLICING TO THE LEFT OF A STATEMENT USING A MUTABLE OBJECT 
    IT WILL NOT CHANGE THE LOCATION IN MEMORY OF THAT OBJECT"""
    
    L[:] = [i for i in L if f(i)]
    
    
    


#run_satisfiesF(L, satisfiesF)

