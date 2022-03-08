# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98
# Then, the output should be:

# '34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


lista = []

while True:
    r = input('Deseja adicionar um número? [S/N] ').upper().strip()
    if r not in 'SsNn':
        print('Responda com [S/N].')
    else:
        if r == 'S':
            n = int(input('Adicione um número: '))
            lista.append(str(n))
        else:
            break

tupla = tuple(lista)
print(lista)
print(tupla)

