#Question
#Write a function to compute 5/0 and use try/except to catch the exceptions.

#Hints
#Use try/except to catch exceptions.

def wrongmath():
    try:
        a = 5/0

    except ZeroDivisionError as ze:
        print("You can't divide by Zero!")

    except:
        print('Go study more')

wrongmath()