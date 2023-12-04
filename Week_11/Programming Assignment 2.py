'''
Write a program that accepts a hash-separated sequence of words as input and
 prints the words in a hash-separated sequence after sorting them alphabetically in reverse order.

Input:
hey#input#bye

Output:
input#hey#bye

'''

#CODE

string=input()
l=string.split("#")
l.sort()
l.reverse()
k="#".join(l)
print(k)