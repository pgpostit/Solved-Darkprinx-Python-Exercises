'''
Question
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

Hints
Use list comprehension to delete a bunch of element from a list.
'''

def isEven(n):
    return n%2!=0

li = [5,6,77,45,22,12,24]
print(list(filter(isEven,li)))