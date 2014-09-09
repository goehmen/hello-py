#!/usr/bin/python

"""This module contains code from
Think Python by Allen B. Downey http://thinkpython.com 
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def polyline(t, length, angle):
    """Draws 3 line segments.

    t: Turtle object
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(3):
        fd(t, length)
        lt(t, angle)


def triangle(t, length):
    """Draws a triangle with n sides.

    t: Turtle
    length: length of each side.
    """
    angle = 360.0/3
    polyline(t, length, angle)

def polygon(t, n, length):
    """Draws a polygon of n triangle segments

    t: Turtle
    n: number of polygon segments
    length:  length of each segment of triangle
    """
    for i in range(n):
        triangle(t,length)
        lt(t, 360.0/n)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
#    pu(bob)
#    fd(bob, radius)
#    lt(bob)
#    pd(bob)
#    polygon(bob, 5, 100)
    polyline(bob, 100,150)
    wait_for_user()

