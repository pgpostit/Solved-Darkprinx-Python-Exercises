'''
Question
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
'''
#professor solution
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2 !=0 and i <=6]
print(li)

#My Solution
lista = [12,24,35,70,88,120,155]
lista = [n for n in lista if lista.index(n) not in (0,2,4,6)]
print(lista)

