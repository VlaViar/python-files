from turtle import *
tracer(0)
a=50
seth(90)
pendown()
screensize(5000,3000)
rt(180)
fd(2*a)
rt(90)
fd(40*a)
rt(90)
fd(2*a)
for d in range(4):
    seth(90)
    circle(-5*a,180)
penup()
for x in range(-60,15):
    for y in range(-15,15):
        setposition(x*a,y*a)
        dot(4,'green')
done()