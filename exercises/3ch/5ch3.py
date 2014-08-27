#!/usr/bin/python

def border_line():
    print '+', '-', '-', '-', '-', '+', '-', '-', '-', '-','+'

def inner_line():
    print '/', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', '/'

def four_inners(f):
    f() 
    f() 
    f() 
    f() 

border_line()
four_inners(inner_line)
border_line()
four_inners(inner_line)
border_line()

#Write a function that draws a similar grid with four rows and four columns



