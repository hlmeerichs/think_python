import turtle
import math

# idea is to change flower function to use triangles instead of leaves

t = turtle.Turtle()

def polygon(t, length, n):
    angle = 360 / n
    for y in range(n):
        t.backward(length)
        t.lt(angle)

def triangle(t, length):
    for y in range(3):
        t.backward(length)
        t.lt(120)

def pie(t, n, length):
    for i in range(n):
        triangle(t, length)
        t.lt(360 / n)

pie(t, 5, 60)


turtle.mainloop()