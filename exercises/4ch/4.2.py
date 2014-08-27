#!/usr/bin/python

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def flower_petal(t, r):
    """Draws a flower by creating an arc with left bend and returning to start with right bend

    t: Turtle
    r: radius
    """
    arc(t, r, 90)
    lt(bob)
    arc(t, r, 90)

def rotation(t,petals):
    """ Spins the turtle x/360 degrees to position for the next petal draw

    t:      turtle
    petals: number of petals to draw.  360/#petals = amount of rotatoin required between each
    """
    turn_angle = int(360/petals)
    lt(t,turn_angle)
    print turn_angle 


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.0001

    # draw a circle centered on the origin
    radius = 50
    petals = 20 
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)

    for i in range(petals):
        flower_petal(bob, radius)
        rotation(bob, petals)

    wait_for_user()
