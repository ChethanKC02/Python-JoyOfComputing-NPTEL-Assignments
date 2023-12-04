'''
Aman likes to study about planets. Every night he goes outside and observe some planets with his telescope. 
Then he guesses the distance of each planet and pen it down. In this process he also pen down his favourite planet position. 
Given the distance of each planet to be unique you need to return position of Aman's favourite planet after sorting all the distances.

Input:
N (No of planets)
L (List of distances of planet)
K (position of Aman's favourite planet in unsorted list)

Output:
Position of Aman's favourite planet in sorted List.

Example:
Input:
5
[4,5,3,2,1]
2
Output:
5

'''

#CODE

N = int(input())
L = [int(i) for i in input().split()]
K = int(input())
a=L[K-1]
L.sort()
print(L.index(a)+1)