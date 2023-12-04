'''
Ram shifted to a new place recently. There are multiple schools near his locality. 
Given the co-ordinates of Ram P(X,Y) and schools near his locality in a nested list, 
find the closest school. Print multiple coordinates in respective order if there exists
multiple schools closest to him. Write a function closestSchool that accepts (X ,Y , L) 
where X and Y are co-ordinates of Ram's house and L contains co-ordinates of different school.

Input:
X, Y (Ram's house co-ordinates)
N (No of schools)
X1 Y1
X2 Y2
.
.
.
X6 Y6

Output:
Closest pont/points to X, Y

'''

#CODE

def closestSchool(x, y, L):
  min=99999
  distance=[]
  for i in L: 
    dis=((x-i[0])**2+(y-i[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis 
  for i in range(len(distance)):
    if distance[i]==min:
        print(L[i])
x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)