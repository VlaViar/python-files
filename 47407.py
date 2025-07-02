from turtle import *
tracer(0)
screensize(2500,2500)
seth(90)
pendown()
z=100
for a in range(4):
    fd(8*z)
    rt(90)
for b in range(3):
    fd(12*z)
    rt(120)
penup()
for x in range(-25,25):
    for y in range(-25,25):
        setposition(x*z,y*z)
        dot(5,'black')
done()