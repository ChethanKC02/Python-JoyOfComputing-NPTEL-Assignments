'''
You are given a list L. Write a program to print first prime number encountered in the list L.
(Treat numbers below and equal to 1 as non prime)

NOTE: Input will be handled by NPTEL interpreter

Input:
[1,2,3,4,5,6,7,8,9]
output:
2

'''

#CODE

L = [int(i)  for i in input().split()]
def is_prime(n):
  if n <= 1:
  	return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True
for i in L:
  if(is_prime(i) and i!=1):
    print(i)
    break