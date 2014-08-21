#!/usr/bin/python

from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle()
print t

def square(t,length):
    for i in range(4):
        fd(t, length)
        lt(t)

#square(t,125)

def polygon(t,length):
    for i in range(2):
        fd(t, length)
        lt(t,45)
        fd(t, length)
        lt(t,135)

#polygon(t,100)

def polygon2(t,length,n):
    t.delay = 0.01
    for i in range(n):
        fd(t, length)
        lt(t,(360/n))

polygon2(t,100,36)

#def circle(t,r):
#    for i in range(n):
#        fd(t, length)
#        lt(t,(360/n))
#
#polygon2(t,100,36)

wait_for_user()
    
