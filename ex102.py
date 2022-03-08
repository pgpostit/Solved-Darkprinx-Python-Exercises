'''
Question
Write a Python program that accepts a string and calculate the number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8
Hints
Use isdigit() and isalpha() function
'''

word = input()
digit,letter = 0,0
for char in word:
    digit+=char.isdigit()
    letter+=char.isalpha()

print('Digit -',digit)
print('Letter -',letter)