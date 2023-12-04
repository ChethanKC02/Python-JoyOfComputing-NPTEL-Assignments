'''
Given a Tuple T, create a function squareT which accepts one argument and returns a tuple containing similar 
elements given in tuple T and its sqaures in sequence. Input and function call is already managed.

Input:
(1,2,3)

Output :
(1,2,3,1,4,9)

'''

#CODE

def squareT(T):
  for i in T:
    T+=(i*i,)
  return T
if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    T = tuple(L)
    ans = squareT(T)
    if type(ans) == type(T):
        print(ans)