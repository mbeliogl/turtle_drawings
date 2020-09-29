
import turtle
import sys

#function to draw trianle 
def drawTriangle(myTurtle, sideLength, numTriangles):
  
    summ = 360/numTriangles
    turn = 120-summ
    
    myTurtle.forward(sideLength)
    myTurtle.right(120)
    myTurtle.forward(sideLength)
    myTurtle.left(turn)



#Main portion of the code that sets the movement of the turtle
def drawPolygon(myTurtle, sideLength, numTriangles):

    myTurtle.left(60)
    for i in range(numTriangles):
        drawTriangle(myTurtle, sideLength, numTriangles)

    myTurtle.right(60) 
  
  
      
def main():
    t = turtle
    t.speed(5)
    numPoints = int(sys.argv[1])
    sideLength = int(sys.argv[2])
    
    drawPolygon(t, sideLength, numPoints)
    turtle.exitonclick()



main()

        
