#!/usr/bin/python

from swampy.TurtleWorld import *
import math

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
        lt(t,(360.0/n))

#polygon2(t,10,36)

def circle(t,r):
    t.delay = 0.01
    length=3.0
    c=(2.0*math.pi*r)
#    c=(2*3*r)
    n=c/length
    polygon2(t,length,n)
    
circle(t,60.0)

#def arc(t,r,angle):
#    t.delay = 0.01
#    length=3
##    c=(2*math.pi*r)
#    c=(2*3*r)
#    n=c/length
#    polygon2(t,length,n)
#    
#arc(t,60,#angle)

wait_for_user()
    
