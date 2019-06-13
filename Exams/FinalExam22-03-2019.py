#! python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:12:23 2019
@author: Tech
Julian Daniel

MIT 6.00.1X Final exam question solutions
"""

# Problem 3
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """

    
    digits = [int(l) for l in s if l.isdigit()]
    if not digits:
        raise ValueError("No digits in String")
    return sum(digits)


#    counter = 0
#    isNumber = False
#    for letter in s:
#        if letter.isdigit():
#            counter += int(letter)
#            isNumber = True
#    if isNumber:
#        return counter
#    raise ValueError("No digits in String")
    

#Problem 4
def max_val(t): 
    """ t, tuple 
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
    """
    def flatten(to_flatten, splatted):
        for i in to_flatten:
            if isinstance(i, (list, tuple)):
                flatten(i, splatted)
            else:
                splatted.append(i)
        return splatted
    return max(flatten(t, []))

# problem 5
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    cipherDict = {i:j for i, j in zip(map_from, map_to)}
    decoded = ''.join([cipherDict[i] for i in code])
    return(cipherDict, decoded)


# Problem 6  Part  1
    
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
# Write a class that implements the specifications below. Do not override any 
# methods of Container.

# 6 Part 1

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs one or more times in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals.keys():
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)
    
# 6 Part 2
    def __add__(self, other);:
        newBag = Bag()
       
        for key in self.vals:
            for i in range(self.vals[key]):
                newBag.insert(key)
        for key in other.vals:
            for i in range(other.vals[key]):
                newBag.inster(key)
        return newBag

# 6 Part 3
        
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals.keys():
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        
        if e in self.vals.keys():
            return True
        return False
    
# Problem 7
        
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        super.__init__(self, center_loc)
        self.tents = []
        self.tents.append(tent_loc)
        
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for tent in self.tents:
            if tent.dist_from(new_tent_loc) < 0.5:
                return False
        self.tents.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        self.tents.remove(tent_loc)
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        self.tents.sort(key = lambda x:x.getX())
        return [str(location) for location in self.tents]
    

    
    
    
    
    
    
    
    
    
   
    
    
    
    






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
