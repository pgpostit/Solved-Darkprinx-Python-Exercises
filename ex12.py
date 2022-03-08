# Question 12
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

#My Solution
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)

print(",".join(values))

#Professor Solution
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))