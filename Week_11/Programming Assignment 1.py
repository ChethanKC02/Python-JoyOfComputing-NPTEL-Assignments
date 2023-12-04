'''
Take 3 sides of a triangle as an input and find whether that triangle is a 
right angled triangle or not. Print 'YES' if a triangle is right angled triangle or 'NO' if it's not.

Input:
3
4
5

Output
YES

'''

#CODE

a=int(input())
b=int(input())
c=int(input())

def is_right(a,b,c):
  return a**2+b**2 == c**2

if is_right(a,b,c) or is_right(b,c,a) or is_right(a,c,b):
  print("YES")
else:
  print("NO")