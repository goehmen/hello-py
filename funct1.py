#!/usr/bin/python

def do_twice(f):
    f()
    f()

def do_twice(f,10):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)

