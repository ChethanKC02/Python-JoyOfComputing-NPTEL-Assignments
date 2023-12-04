'''
Write a function whole(N) which takes a number N and return the sum of first N whole number. Write the program using recursion.

Input:
N
Output:
sum of whole numbers till N

Example:
Input:
3
Output:
6

'''

#CODE

def whole(n):
  if(n==0):
    return 0
  return n+whole(n-1)
  
N = int(input())
print(whole(N))