'''
Given a list of strings, write a program to write sort the list of strings 
on the basis of last character of each string.

Input:
L = ['ram', 'shyam', 'lakshami']

Output:
['lakshami', 'ram', 'shyam']

'''

#CODE

k=input()
L=k.split(" ")
li=[]

for i in L:
  k=i[::-1]
  li.append(k)

li.sort()
new_list=[]
for i in li:
  k=i[::-1]
  new_list.append(k)

print(new_list,end=" ")