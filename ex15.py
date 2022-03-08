#Question 15
#Question:
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#Suppose the following input is supplied to the program:

#9
#Then, the output should be:

#11106
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

#Professor Solution

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)