import turtle
import math

turtle.Turtle().speed("fastest")
turtle.tracer(0, 0)

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

def flower(t, n, r, angle):
    """Draws a flower using:
    t: turtle
    n: n * leaves
    r: radius of one leave
    angle: angle of each leave
    """
    for i in range(n):
        leave(t, r, angle)
        t.lt(360 / n)

flower(tt, 18, 200, 90)
flower(t, 12, 70, 60)

# next step add circle in the center, figure out overlapping
turtle.update()
turtle.mainloop()
