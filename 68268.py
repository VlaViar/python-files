from turtle import *
tracer(0)
x=12
a=20
pendown()
seth(90)
screensize(3000,3000)
fd((x+2)*a)
for b in range(4):
    fd(x*a)
    rt(90)
    fd((x+2)*a)
rt(90)
fd(2*x*a)
for b in range(4):
    rt(90)
    fd((3*x-1)*a)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setposition(x*a,y*a)
        dot(6,'red')
done()