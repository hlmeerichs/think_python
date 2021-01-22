import turtle
import math

t = turtle.Turtle()
t.shape("arrow")
t.color("red", "orange")

t.hideturtle()
t.speed(100)
t.begin_fill()

def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and angle (in degrees) 
    between them. t is a turtle
    """  
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc_leaves(t, r, angle):
    """
    draws an arch with given radius r and angle
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n, step_length, step_angle)

for i in range (18): 
    arc_leaves(t, 100, 90)
    t.left(120)

t.end_fill()

turtle.mainloop()