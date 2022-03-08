#Question:
#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

#Hints:
#Use filter() to filter elements of a list.Use lambda to define anonymous functions.

def even(x):
    return x%2==0

li = [i for i in range(1,21)]
print(list(filter(even,range(1,21))))
