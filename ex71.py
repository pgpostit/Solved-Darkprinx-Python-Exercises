'''
Question 71
Question
Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
'''
import random
lst = [i for i in range (10,150) if i%35==0]
print(random.choice(lst))