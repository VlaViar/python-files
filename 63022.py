from turtle import *
tracer(0)
a=20
seth(90)
rt(90)
pendown()
screensize(3000,3000)
for b in range(4):
    forward(14*a)
    rt(90)
for c in range(5):
    forward(5*a)
    rt(45)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setposition(x*a,y*a)
        dot(5,'red')
done()