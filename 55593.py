from turtle import *
tracer (0)
screensize (3000, 3000)
a = 20
x = 15
seth (90)
pendown ()
for b in range (4):
    fd (x * a)
    rt (90)
    fd (x * a)
    lt (90)
    fd (x * a)
    rt (90)
penup ()
for c in range (-75,75):
    for d in range (-75,75):
        setposition(c*a,d*a)
        dot(4,'red')
done()