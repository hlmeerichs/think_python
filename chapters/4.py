# this is the fourth chapter: case study
# work started on 20.01

# import turtle

# b = turtle.Turtle()
# b.shape("arrow")
# b.backward(100) # distance in pixels
# for x in range(4):
#     b.fd(100)
#     b.lt(90) #notice how arrow is back in starting postition: the last .lt(90) has this effect

# a = turtle.Turtle()
# a.shape("turtle")
# a.fd(100)
# a.lt(90)
# a.fd(100)
# a.lt(90)
# a.fd(100)
# a.lt(90)
# a.fd(100)

# turtle.mainloop() # has to be in the end!!

# for i in range(4): 
#    print('four!')

# 4.3

import turtle
import math

t = turtle.Turtle() # for clean code, define this here and not later
t.shape("arrow") # -""-

# exercise 1 and 2
def square(t, length):
    for y in range(4):
        t.backward(length)
        t.lt(90)

square(t, 75)

# exercise 3
def polygon(t, length, n):
    angle = 360 / n
    for y in range(n):
        t.backward(length)
        t.lt(angle)

alice = turtle.Turtle
polygon(t, length=75, n=9) # they are called keyword arguments

# exercise 4
def circle(t, r): # circle with radius r
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3 # adding 3 guarantees that the polygon has at least three sides
    length = circumference / n # small enough to make the circle look good, but big enough to be efficient
    polygon(t, length, n) # to not clutter up the interface, it is better to choose assign an appropriate value to the local variable n

circle(t, 190) 

# exercise 5
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360 # circumference = only part of the circle
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(t, 90, 90)

# refactoring code: we have accquired an understanding of our problem and can thus use this knowledge to simplify our code
def polyline(t, n, length, angle):
    """Draws n line segments with the given length and angle (in degrees) 
    between them. t is a turtle.""" # this is a docstring!!!!
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc_new(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n, step_length, step_angle)

def circle_new(t, r):
    arc_new(t, r, 360)

circle_new(t, 25)
arc_new(t,50, 360)

turtle.mainloop()

# encapsulation and generalization:
# (1) start by writing a small program with no function definitions
# (2) once you get the program working, identify a coherent piece in 
#     a function and give it a name
# (3) generalize the function by adding appropriate parameters
# (4) repeat steps 1-3 until you have a set of working functions.
#     Copy and paste working code to avoid retyping (and re-debugging)
# (5) look for opportunities to improve the program by refactoring. For
#     example, if you have similiar code in several places, consider
#     factoring it into an appropriately general function