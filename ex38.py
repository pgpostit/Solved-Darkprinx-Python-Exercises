#Question:
#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

#Hints:
#Use [n1:n2] notation to get a slice from a tuple.

#My Solution
tpl = (1,2,3,4,5,6,7,8,9,10)
def printtpl(tpl):
    half = int(len(tpl)/2)
    for i in range(1,half+1):
        if i < half:
            print(i, end=', ')
        else:
            print(i)

    for i in range(half, int(len(tpl)+1)):
        if i < int(len(tpl)):
            print(i,end=', ')
        else:
            print(i)

printtpl(tpl)

#Professor Solution
tpl2 = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl2[i],end = ' ')
print()
for i in range(5,10):
    print(tpl2[i],end = ' ')