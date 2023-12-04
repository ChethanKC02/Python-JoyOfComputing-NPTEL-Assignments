'''
Given a string S, write a function replaceV that accepts a string and replace the occurrences 
of 3 consecutive vowels with _ in that string. Make sure to return the answer string.

Input:
aaahellooo

Output:
_hell_

'''

#CODE

def replaceV(S):
  vowel=['a','e','i','o','u','A','E','I','O','U']
  new_string=''
  length=len(S)
  i=int(0)
  while i < length:
    if i<length and S[i] in vowel and i+1<length and S[i+1] in vowel and i+2<length and S[i+2] in vowel:
      i+=2
      new_string+='_'
    else:
      new_string+=S[i]
    i+=1
  return new_string
S = input()
print(replaceV(S))