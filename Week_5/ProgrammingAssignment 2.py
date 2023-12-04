'''
You are given a list L. Write a function uniqueE which will return a
list of unique elements is the list L in sorted order. 
(Unique element means it should appear in list L only once.)

NOTE: Input will be handled by NPTEL interpreter

Input:
[1,2,3,3,4,4,2,5,6,7]
Output:
[1,5,6,7]

''' 

#CODE

def uniqueE(lst):
  element_count = {}
  for num in lst:
    if num in element_count:
      element_count[num] += 1
    else:
      element_count[num] = 1
  unique_elements = [num for num, count in element_count.items() if count == 1]
  unique_elements.sort()
  return unique_elements

L = [int(i) for i in input().split()]
print(uniqueE(L))