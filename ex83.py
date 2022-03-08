'''
Question
By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
'''

#Professor Solution
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i < 3 or i > 4]
print(li)

#My Solution
lst = [12,24,35,70,88,120,155]
lst = [i for i in lst if lst.index(i) not in (1,3)]
print(lst)

