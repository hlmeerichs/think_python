# exercise 2; turtle flowers
#
# before trying to solve the coding side of a problem, first translate to and
# understand its mathematical nature

import turtle
import math # flower two and three have circles in them

t = turtle.Turtle()
t = t.shape("arrow")

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

def leave_one(t, l, a):
    """
    t(=turtle) draws a leave with l (=length in pixels) and a(=angle in degrees)
    """
    for i in range(2):
        arc_leaves(t, l, 180)
        t.lt(a)

b = turtle.Turtle()
leave_one(b, 50, 180)