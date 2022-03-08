#Question 13
#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.

#Suppose the following input is supplied to the program:

#hello world! 123
#Then, the output should be:

#LETTERS 10
#DIGITS 3
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

words = input()
count_num = 0
count_letters = 0
for i in words:
    if i.isnumeric():
        count_num+=1
    if i.isalpha():
        count_letters+=1

print(f'NUMBERS: {count_num}\nLETTERS: {count_letters}')


