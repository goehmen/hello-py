#!/usr/bin/python

def do_twice(f, gerg):
    f(gerg)
    f(gerg)

def print_twice(card):
    print card
    print card

do_twice(print_twice, 'spam') 
print ''

def do_four(f, mary):
    do_twice(f, mary)
    do_twice(f, mary)

do_four(print_twice, 'baby,yeah!!!!!')
print ''


# before ending, i want to be able to pass in the string as an arg to the script itself

