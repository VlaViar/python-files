from turtle  import *
tracer(0)
screensize(3000,3000)
pendown()
seth(90)
z=25
for a in range(4):
    fd(8*z)
    rt(90)
    fd(8*z)
    rt(90)
penup()
for x in range(-15,15):
    for y in range(-15,15):
        setposition(x*z,y*z)
        dot(5,'blue')
done()