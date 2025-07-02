from turtle import *
tracer(0)
screensize(3000,3000)
seth(90)
pendown()
p=30
for a in range(4):
    for b in range(4):
        fd(6*p)
        rt(90)
    fd(10*p)
    rt(90)
    fd(3*p)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setposition(x*p,y*p)
        dot(5,'orange')
done()