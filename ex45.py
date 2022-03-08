#Question:
#Define a class named American which has a static method called printNationality.

#Hints:
#Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.

class American:
    @staticmethod
    def printNationality():
        print("I am American")


american = American()
american.printNationality()
American.printNationality()