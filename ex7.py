#Question:
#_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*

#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

#Then, the output of the program should be:

#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#Hints:
#Note: In case of input data being supplied to the question, it should be assumed
# to be a console input in a comma-separated form.

i = int(input('Value of i: '))
j = int(input('Value of j: '))

#My Solution
def cria_matriz(i, j):
    matriz = []
    for linha in range(i):
        vetor = []
        for coluna in range(j):
                vetor.append(linha*coluna)
        matriz.append(vetor)
    return matriz

print(cria_matriz(i,j))

#Teacher's solution
x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)