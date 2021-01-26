import turtle
import math

turtle.Turtle().speed(100)

t = turtle.Turtle()
tt = turtle.Turtle()



def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def leave(t, r, angle):
    """Draws a leave using:

    t: turtle
    r: radius
    angle: angle between arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

leave(tt, 200, 30)

# next step build actual flower, also incorporate circle in the middle
turtle.mainloop()