'''
Given a sqaure matrix M, write a function DiagCalc which calculate the sum of left 
and right diagonals and print it respectively.

Input:
A matrix M 
[[1,2,3],[3,4,5],[6,7,8]] 

Output :
13
13

'''

#CODE

def DiagCalc(M):
  b,d=0,0
  le=len(M)
  for i in range(le):
    b+=M[i][le-i-1]
    d+=M[i][i]
  print(d)
  print(b)
    
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

DiagCalc(M)