#Question:
#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

#Hints:
#Use if statement to judge condition.

x = str(input().lower())
if x == 'yes':
    print('Yes')
else:
    print('No')