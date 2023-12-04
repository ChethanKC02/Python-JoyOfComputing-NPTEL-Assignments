'''
Given a matrix M write a function snake that accepts a matrix M and returns a list which 
contain elements in snake pattern of matrix M. 

Input:
A matrix M
91 59 21 63 
81 39 56 8 
28 43 61 58 
51 82 45 57

Output:
[91, 59, 21, 63,
  8, 56, 39, 81, 
 28, 43, 61, 58,
 51, 82, 45, 57]

'''

#CODE

def snake(M):
  Mat=[]
  r,c=len(M),len(M[0])
  for i in range(r):
    if i%2==0:
      for j in range(c):
        Mat.append(M[i][j])
    else:
      for j in range(c -1,-1,-1):
        Mat.append(M[i][j])
  return Mat
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))