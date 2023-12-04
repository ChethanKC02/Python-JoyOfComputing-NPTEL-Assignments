'''
Given a string s write a program to convert uppercase letters into lowercase and lowercase letters 
into uppercase. Also print the resultant string.

Input:
The Joy Of Computing

Output
tHE jOY oF cOMPUTING

'''

#CODE

S=input()
new=""
for i in S:
  if i.isupper():
    new+=i.lower()
  elif i.islower():
    new+=i.upper()
  else:
    new+=i
print(new)