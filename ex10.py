#Question 10
#Question
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after
# removing all duplicate words and sorting them alphanumerically.

#Suppose the following input is supplied to the program:

#hello world and practice makes perfect and hello world again
#Then, the output should be:

#again and hello makes perfect practice world
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

#Professor Solution
word = input().split()

for i in word:
    if word.count(i) > 1:
        word.remove(i)

word.sort()
print(" ".join(word))

#My Solution
word2 = input().split()
word2 = set(sorted(word2))
print(" ".join(word))