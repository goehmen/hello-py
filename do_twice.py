#!/usr/bin/python

def do_twice(f, g):
    f()
    f()

def print_f():
    print f

do_twice(print_f)

