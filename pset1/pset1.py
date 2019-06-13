# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:26:37 2018

@author: Tech
"""
#import string
vowels = 'aeiou'
count = 0
#s = string.ascii_lowercase


"""part 1"""

count = 0
for letters in s:
    if letters in 'aeiou':
        count += 1
print('Number of vowels: {}'.format(count))

count = len([v for v in s if v in 'aeiou'])
print('Number of vowels: {}'.format(count))


 
"""part 2"""

count = 0
for digit in range(len(s) - 2):
    if s[digit:digit + 3] == 'bob' : 
        count += 1
print('Number of times bob occurs is: {}'.format(count))


"""part 3"""


s = 'abcdefghijklmnopqrstuvwxyz'

actual_ans, current_len_ans, first_letter = s[0] , 1 , 0

for letter in range(1, len(s)):
    #if current letter is still in alphabetial order conintue counting 
    if s[letter] >= s[letter-1]:
        current_len_ans += 1
        # if current answer > actual answer, update actual answer
        if current_len_ans > len(actual_ans):
            actual_ans = s[first_letter:letter+1]
    #if not in alphabetical order restart counting 
    else: 
        first_letter, current_len_ans = letter , 1

print('Longest substring in alphabetical order is: {}'.format(actual_ans))









a b c d e f g h i j  k  l

0 1 2 3 4 5 6 7 8 9 10  11 
