#Question
#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

#Hints
#Use def methodName(self) to define a method.

class Rectangle():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght*self.width


arec = Rectangle(2,10)
print(arec.area())