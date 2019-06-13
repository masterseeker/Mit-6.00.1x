# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:11:06 2018

@author: Tech


"""

"""   part 1 """

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

"""   part 2  """

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for letter in secretWord: 
        if letter in lettersGuessed:
            guessedWord += letter
        else: 
            guessedWord += '_ '
    return guessedWord


"""    part 3     """
            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    availableLetters = ''
    
    for letter in string.ascii_lowercase
        if letter not in lettersGuessed:
            availableLetters += letter
            
    return availableLetters
    
  
            