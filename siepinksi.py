
import turtle
import sys 


# need to get a middle point #
def middlePoint(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2
    return(x, y)

# this function draws a regular triangle (level 0 triangle) #    
def drawTriangle(t, color, p1, p2, p3):
    t.fillcolor(color)
    t.up()
    t.goto(p1[0], p1[1])
    t.down()
    t.begin_fill()
    t.goto(p2[0], p2[1])
    t.goto(p3[0], p3[1])
    t.goto(p1[0], p1[1])
    t.end_fill()
    

def sierpinski(t, p1, p2, p3, numLevels):
    
    colors = [(0,150,189),(4,150,116),(216,95,30),(193,33,57),(129,41,199),
                (102,205,135),(51,187,204)]

    drawTriangle(t, colors[numLevels], p1, p2, p3)

    if numLevels > 0:    
        sierpinski(t, p1, middlePoint(p1,p2), middlePoint(p1, p3), numLevels - 1)
        sierpinski(t, p2, middlePoint(p1,p2), middlePoint(p2, p3), numLevels - 1)
        sierpinski(t, p3, middlePoint(p3,p2), middlePoint(p1, p3), numLevels - 1)
        
def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    numLevels = int(sys.argv[1])
    sierpinski(t, (-200, -100), (0,200), (200,-100), numLevels)
    t.hideturtle()
    
    turtle.exitonclick()

main()
