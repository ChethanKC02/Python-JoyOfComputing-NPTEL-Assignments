'''
Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.

Input :
A matrix M
[[1,2,3],[4,5,6],[7,8,9]]

Output:
Transpose of M
[[1,4,7],[2,5,8],[3,6,9]]

'''

#CODE

def Transpose(M):
  r,c=len(M),len(M[0])
  t=[[ 0 for i in range(r)] for _ in range(c)]
  for i in range(r):
    for j in range(c):
      t[j][i]=M[i][j]
  return t
  
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))