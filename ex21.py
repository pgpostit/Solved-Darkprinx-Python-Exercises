#Question 21
#A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:

#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps. Please write a program to compute the distance from current
# position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:

#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Then, the output of the program should be:

#2

#Importing the sqrt function to use the euclidiand distance formula
import math
x = 0
y = 0

#Function to calculate the distance
def dist(x, y):
    dist = round(math.sqrt(x ** 2 + y ** 2))
    return dist

#Movement information input
while True:
    move = input().split()
    if len(move) == 0:
        break
    if move[0] == 'UP':                                #move[0] as the direction
        y += int(move[1])                              #move[1] representing the steps
    if move[0] == 'DOWN':
        y -= int(move[1])
    if move[0] == 'LEFT':
        x -= int(move[1])
    if move[0] == 'RIGHT':
        x += int(move[1])

#Movement output
print(f'''The robot moved from the point Y(0) to the point Y({y}) on the vertical plan and from the point 
X(0) to the point X({x}) on the horizontal plan''')
print(f'The euclidian distance of the bot to the original poisition is {dist(x,y)}')