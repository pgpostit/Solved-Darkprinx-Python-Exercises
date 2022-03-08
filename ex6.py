#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 _ C _ D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
#Hints:
#If the output received is in decimal form, it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26).
# In case of input data being supplied to the question, it should be assumed to be a console input.
from math import sqrt
c = 50
h = 30
def calc(d):
    return sqrt(2*c*d/h)
#MY SOLUTION
lista = []
while True:
    r = input('Deseja adicionar um número? [S/N] ').upper().strip()
    if r not in 'SsNn':
        print('Não entendi. Responda com S/N.')
    else:
        if r == 'S':
            n = int(input('Adicione um número: '))
            lista.append(n)
        if r== 'N':
            break

for i in lista:
        print(str(int(calc(int(i)))), end=',')

#USER'S SOLUTION
D = [int(i) for i in input('Add a number: ').split(',')] #splits , and set up the numbers in list
D = [int(i) for i in D] #conver the numbers to int
D = [calc(i) for i in D] #use the function calc
D = [round(i) for i in D] #round the numbers in list
D = (str(i) for i in D) #converts to string to use join
print(",".join(D)) #printing

