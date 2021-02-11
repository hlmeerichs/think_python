""" alphabet functions

> alphabet has 26 letters
    > uses parts of circles (o a q u e p s d f g h c b n m)
        > and simple lines 
thus, a circle function and simple lines will proove sufficient. for writing the cursor
needs to reset, using pu and pd. Also, radius of circles and line length need to stay 
somewhat consistent
"""

import turtle
import math

t = turtle.Turtle()

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

def draw_o():
    arc(t, 10, 360)    
    
turtle.mainloop()