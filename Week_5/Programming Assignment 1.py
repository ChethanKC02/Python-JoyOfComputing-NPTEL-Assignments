'''
You are given a string S. Write a function count_letters which will return a dictionary containing letters 
(including special character) in string S as keys and their count in string S as values.

NOTE: Input will be handled by NPTEL interpreter

Input: 
The Joy of computing 

Output: 
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}

'''

#CODE

def count_letters(S):
  letter_count = {}
  for char in S:
    if char in letter_count:
      letter_count[char] += 1
    else:
      letter_count[char] = 1
  return letter_count
S = input()
d = count_letters(S)
d1 = {}
for i in S:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
if d1 == d:
    print('yes')
else:
    print('no')