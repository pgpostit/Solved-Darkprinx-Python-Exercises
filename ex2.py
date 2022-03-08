# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

#My Solution
def fact_calculator(factorial):
    i = factorial - 1
    print(f'The factor of {factorial} is: {factorial} x ', end='')
    while i > 0:
      if i > 1:
        print(f'{i}! x ',end='')
      else:
        print(f'{i}! ')
      factorial = factorial * i
      i -=1
    return factorial

fact = int(input('Say the number to be factorialized: '))
print(f'= {fact_calculator(fact)}')

#Lambda function solution
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))


