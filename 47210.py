from turtle import *
tracer(0)
screensize(3000,3000)
b=50
left(90)
pendown()
for a in range(7):
    forward(10*b)
    rt(120)
penup()
for x in range(-15,15):
    for y in range(-15,15):
        setposition(x*b,y*b)
        dot(5,'red')
done()