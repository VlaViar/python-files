from turtle import *
tracer(0)
screensize(3000,3000)
seth(90)
pendown()
p=50
for a in range(4):
    fd(14*p)
    rt(90)
for b in range(5):
    fd(5*p)
    rt(45)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setposition(x*p,y*p)
        dot(3,'red')
done()