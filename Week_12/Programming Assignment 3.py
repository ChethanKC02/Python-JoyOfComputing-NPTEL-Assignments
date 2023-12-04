'''
Given a student's roll number in the following format rollNumber@institute.edu.in,
 write a program to find the roll number and institute name of the student.

Input:
roll@institute.edu.in

Output:
roll institute

'''

#CODE

l=input()
print(l[:l.index("@")],l[l.index("@")+1:l.index(".")],end="")