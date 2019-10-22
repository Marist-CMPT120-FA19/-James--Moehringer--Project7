# James Moehringer
# james.moehringer1@marist.edu
# This project is a simple archery game created with python


from graphics import*
import math

def archer (p, ring):
    x= p.getX()- ring.getCenter().getX()
    y= p.getY()- ring.getCenter().getY()
    d= math.sqrt(x**2 + y**2)
    return d <= ring.getRadius()

def main():
    win = GraphWin("Board", 600, 600)
    white= Circle(Point(300, 300), 150)
    white.setFill("white")
    white.draw(win)
    black= Circle(Point(300, 300), 120)
    black.setFill("black")
    black.draw(win)
    blue= Circle(Point(300, 300), 90)
    blue.setFill("blue")
    blue.draw(win)
    red= Circle(Point(300, 300), 60)
    red.setFill("red")
    red.draw(win)
    yellow= Circle(Point(300, 300), 30)
    yellow.setFill("yellow")
    yellow.draw(win)

    message= Text(Point(100, 25), "Your total score is : 0")
    message.draw(win)

    total = 0

    for i in range (0,5):
        p = win.getMouse()
        hit= Circle(p, 5)
        hit.setFill("green")
        hit.setOutline("green")
        hit.draw(win)
        if (archer(p, yellow)):
            total = total + 9
            message2= Text(Point(100, 50), "score : 9")
            message2.draw(win)
        elif (archer(p, red)):
            total = total + 7
            message3= Text(Point(100, 60), "score : 7")
            message3.draw(win)
        elif (archer(p, blue)):
            total = total + 5
            message4= Text(Point(100, 70), "score : 5")
            message4.draw(win)
        elif (archer(p, black)):
            total = total + 3
            message5= Text(Point(100, 80), "score : 3")
            message5.draw(win)
        elif (archer(p, white)):
            total = total + 1
            message6= Text(Point(100, 90), "score : 1")
            message6.draw(win)
        else:
            total = total + 0
            message= Text(Point(100, 100), "score : 0")
            message.draw(win)
        total= total

    message.setText("Your total score is : " + str(total))
    win.getMouse()
    win.close()

main()
    
