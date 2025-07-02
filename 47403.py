from turtle import *
tracer(0)
a=25
seth(90)
pendown()
screensize(3000,3000)
for b in range(4):
    forward(12*a)
    right(90)
right(30)
for c in range(3):
    forward(8*a)
    right(60)
    forward(8*a)
    right(120)
penup()
for x in range(-15,15):
    for y in range(-15,15):
        setposition(x*a,y*a)
        dot(4,'green')
done()