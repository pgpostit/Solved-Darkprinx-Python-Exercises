#Question
#Define a custom exception class which takes a string message as attribute.

#Hints
#To define a custom exception, we need to define a class inherited from Exception.

class CustomException (Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

num = int(input())

try:
    if num < 0:
        raise CustomException("Input is less than 0")
    elif num > 10:
        raise CustomException("Input is greater than 10")
except CustomException as ce:
    print("the error raised: " + ce.message)