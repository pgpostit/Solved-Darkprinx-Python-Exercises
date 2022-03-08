'''
Question
You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1
Hints
Count frequency with dictionary and sort by Value from dictionary Items
'''

word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct:
    print(i[0],i[1])

'''Solution by: yuan1z'''

X = input()
my_set = set(X)
arr = []
for item in my_set:
    arr.append([item,X.count(item)])
tmp = sorted(arr,key = lambda x: (-x[1],x[0]))

for i in tmp:
    print(i[0]+' '+str(i[1]))

    
'''Solution by: StartZer0'''

s = list(input())

dict_count_ = {k:s.count(k) for k in s}
list_of_tuples = [(k,v) for k,v in dict_count_.items()]
list_of_tuples.sort(key = lambda x: x[1], reverse = True)

for item in list_of_tuples:
  print(item[0], item[1])

