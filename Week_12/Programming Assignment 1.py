'''
Write a program to an integer as an input and reverse that integer.

Input:
A single integer.

Output:
Reverse number of that integer.

Example:
Input:
54321

Output:
12345

'''

#CODE

a=int(input())
n=0

while a>0:
  n+=a%10
  n*=10
  a=(int)(a/10)
  
n=int(n/10)
print(n)