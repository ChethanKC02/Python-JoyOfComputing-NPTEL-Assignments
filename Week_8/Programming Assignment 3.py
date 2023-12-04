'''
Given a list L, write a program to shift all zeroes in list L towards the right 
by maintaining the order of the list. Also print the new list.

Input:
[0,1,0,3,12]
Output:
[1,3,12,0,0]

'''

#CODE

n = 10
L = list(map(int, input().split()))
new_li1=[]
new_li2=[]
for i in L:
  if i!=0:
    new_li1.append(i)
  else:
    new_li2.append(i)
new_li1+=new_li2
print(new_li1)