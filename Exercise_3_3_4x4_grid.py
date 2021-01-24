#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sat Jan 23 15:11:15 2021
@author: luis vargas rojas
Assignment: 3_3 - Spring 2021 ABE 65100 -Learning the Basics
'''

''' Function that creates a 4x4 grid. It is possible to indicate the number of rows 
to create an nx4 grid if you declare the rows argument
'''
def print_grid():
    rows = 4 # change this value if you wish to increase the number of rows, or put it as an argument

    # Controls the number of horizontal and vertical lines that must be printed, and when they must be printed
    for n in range(0, (rows * 5) + 1): 
        if n == 0 or n % 5 == 0:
            print('+ ', 4 * '- ', '+ ', 4 * '- ', '+ ', 4 * '- ', '+ ', 4 * '- ', '+', sep='')
        else:
            print('| ', 4 * '  ', '| ', 4 * '  ', '| ', 4 * '  ', '| ', 4 * '  ', '|', sep='')


# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':

    # make this statement produce a 4x4 grid on the screen
    print_grid()
