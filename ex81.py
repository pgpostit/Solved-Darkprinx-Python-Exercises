'''
Question 81
Question
By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
'''
def div35(n):
    return n%35==0

lst = [12,24,35,70,88,120,155]
print(list(filter(div35,lst)))