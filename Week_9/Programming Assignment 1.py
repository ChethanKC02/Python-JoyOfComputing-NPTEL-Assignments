'''
Given two string s1 and s2, write a function subStr which accepts two parameters s1 and s2
and will return True if a s2 is a substring of s1 otherwise return False.
A substring is a is a contiguous sequence of characters within a string. 

Input:
bananamania
nana
Output:
True

Input:
aabbcc
abc
output:
False

'''

#CODE

def subStr(s1,s2):
  if s2 in s1:
    return True
  else:
    return False
    		
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2))