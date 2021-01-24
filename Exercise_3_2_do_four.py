#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sat Jan 23 15:11:15 2021
@author: luis vargas rojas
Assignment: 3_2 - Spring 2021 ABE 65100 -Learning the Basics
'''

## Start function do_twice
''' Function that runs a fuction twice. Func is the name of the function, arg is 
the argument of the function that will be ran ''' 
def do_twice(func, arg):
    for _ in range(2):
        func(arg)
## /end function do_twice

## Start function print_twice
''' Function that prints an argument twice in separate lines, arg is 
the argument that will be printed ''' 
def print_twice(arg):
    print(arg,'\n', arg, sep='')
## /end function print_twice

## Start function do_four
''' Function that runs a fuction four times. Func is the name of the function, arg is 
the argument of the function that will be ran''' 
def do_four(func, arg):
    for _ in range(4):
        func(arg)
## /end function do_four


# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':


    # start by making this work (and adding your own comments)
    do_twice(print, 'spam')

    # then make this statement work (do not forget to remove the #)
    do_twice(print_twice, 'spam')

    # finally, make this statement work
    do_four(print_twice, 'spam')
    
