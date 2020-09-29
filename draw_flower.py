
import turtle

import sys

#Primary function that defines the movement of the turle
def drawSquare(myTurtle, numSquare,  sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
        
#Main function to run as a python program        
def main():
    t = turtle
    numSquare = int(sys.argv[1])
    sideLength = int(sys.argv[2])
    for i in range(numSquare):
        drawSquare(t, numSquare,  sideLength)
        t.left(18)
    turtle.exitonclick()

main()
