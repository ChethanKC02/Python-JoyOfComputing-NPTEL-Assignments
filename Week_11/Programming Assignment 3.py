'''
Write a program which takes two integer a and b and prints all composite numbers 
between a and b.(both numbers are inclusive)

Input:
10
20

Output:
10
12
14
15
16
18
20

'''

#CODE
a=int(input())
b=int(input())
for i in range(a,b+1):
  count=0
  for j in range(2,i+1):
    if i%j==0:
      count+=1
    if count>1:
      break
  if count>1:
    print(i)