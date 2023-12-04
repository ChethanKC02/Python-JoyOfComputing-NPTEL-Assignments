'''
Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone
to read it without his permission. So he shifted every small letter in the sentence 
by -2 position and every capital letter by -3 position. (If the letter is c, 
after shifting to by -2 position it changes to a, and for D new letter will be A).
But the letter is too long and Romeo does not have enough time to encrypt his whole letter. 
Write a program to help Romeo which prints the encrypted message. You can assume there are no special 
characters except spaces and numeric value.

Input:
A string S 
Output:
Encrypted string 

Example

Input:
Hello Juliet
Output:
Ecjjm Gsjgcr

'''

#CODE

S = input()
import string
lc=string.ascii_lowercase
uc=string.ascii_uppercase
ans=str("")
for i in S:
  if i in lc:
    ans+=lc[lc.index(i)-2]
  elif i in uc:
    ans+=uc[uc.index(i)-3]
  else:
    ans+=i
print(ans)