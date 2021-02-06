import turtle
import math

# idea is to change flower function to use triangles instead of leaves
# math behind this: the inner angle of each triangle summed up needs to be 360

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
    p = n * 2
    for i in range(p):
        triangle(t, length)
        t.lt(360 / p)


pie(t, 3, 60)

turtle.mainloop()
