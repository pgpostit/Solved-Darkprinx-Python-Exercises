'''
Question
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Hints
Use wrap function of textwrap module
'''

import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

"""Solution by: mishrasunny-coder
"""
import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))


"""solution by  : Prashanth
"""
from textwrap import wrap
x = str(input(': '))
w = int(input())
z = list(wrap(x, w))
for i in z:
    print(i)


"""solution by  : saxenaharsh24
"""
import textwrap
string = input('')
print('\n'.join(textwrap.wrap(string, width= int(input('')))))


"""solution by  : popomaticbubble
"""
import itertools
string = input("> ")
width_length = int(input("What is the width of the groupings? "))

def grouper(string, width):
    iters = [iter(string)] * width
    return itertools.zip_longest(*iters, fillvalue='')

def displayer(groups):
    for x in groups:
        if x == '':
            continue
        else:
            print(''.join(x))

displayer(grouper(string, width_length))