#Question 17
#Question:
#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:

#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:

#D 300
#D 300
#W 200
#D 100
#Then, the output should be:

#500
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

#MY SOLUTION
S = 0
while True:
    T = input().split(' ')
    if T[0] == 'D':
        S += int(T[1])
    if T[0] == 'W':
        S -= int(T[1])
    if T[0] == '':
        break

print(S)