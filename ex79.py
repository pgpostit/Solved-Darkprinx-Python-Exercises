'''
Question
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints
Use list[index] notation to get a element from a list.
'''
first = ['I', 'You']
second = ['Play', 'Love']
third = ['Hockey','Football']

for i in first:
    for j in second:
        for k in third:
            print(f'{i} {j} {k}')