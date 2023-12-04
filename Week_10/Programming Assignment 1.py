'''
Given a list L write a program to make a new list to fix 
the indexes of numbers to in list L to its same value in the new list.
Put 0 at remaining indexes. Also print the elements of the new list in the single line.

Input:
[1,5,6]

Output:
0 1 0 0 0 5 6

'''

#CODE

L = list(map(int, input().split()))
new = [0]*(max(L)+1)
for i in range(len(new)):
  if i in L:
	  print(i,end=" ")
  else:
    print(0,end=" ")