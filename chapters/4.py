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

# exercise 1 and 2
def square(t, length):
    t = turtle.Turtle()
    t.shape("classic")
    for y in range(4):
        t.backward(length)
        t.lt(90)

square("i", 75)

# exercise 3
def polygon(t, length, n):
    t = turtle.Turtle()
    t.shape("classic")
    for y in range(n):
        t.backward(length)
        t.lt(360 / n)

polygon("o", 75, 9)

# exercise 4
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100 
    length = circumference / n 
    polygon(t, length, n)

circle("t", 190) 

# exercise 5
def arc(r, angle):
    angle = 
    circle("a", 190)
    


turtle.mainloop()
