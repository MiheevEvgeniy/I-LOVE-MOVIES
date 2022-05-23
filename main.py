import turtle as t
from turtle import *
color('black', 'yellow')
t.pensize(2)
t.speed(0)
angle1=0
angle2=120
while True:
    left(angle1)
    forward(50)
    right(angle2)
    forward(100)
    back(angle1/2)
    forward(30)
    right(angle2-50)
    forward(100)
    penup()
    if angle1>=360:
        angle1=0
    t.setheading(90)
    angle1+=30
    goto(0,0)
    pendown()
end_fill()
done()