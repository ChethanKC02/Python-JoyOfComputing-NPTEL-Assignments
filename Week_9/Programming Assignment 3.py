'''
Given an integer n, print all the indexes of numbers in that integer from left to right.

Input:
122345

Output:
1 0 
2 1 2
3 3
4 4
5 5

'''

#CODE

n = int(input())
idp=dict()
for i in str(n):
  idp[i]=[]
  for j in range(len(str(n))):
    if i==str(n)[j]:
      idp[i]+=[j] 
for k in idp:
    print(k,*idp[k],"") 