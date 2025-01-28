#!/usr/bin/python

def next_iter(x, y, x0, y0):
    """Returns the next iteration value given the current one and the original point"""
    new_x = x0 + x**2 - y**2
    new_y = y0 + 2 * x * y
    return new_x , new_y     # Note: this returns the two elements in a tuple.

def is_unbound(x, y, limit=2):
    """Check is the modulus of the iteration is above a limit"""
    return (x*x + y*y)**0.5 > limit

def is_part_of_set(x, y, nb_iter=10):
    """Returns True if the coordinates x, y are part of the mandelbrot set.
    For details about the mandelbrot set see 
    https://en.wikipedia.org/wiki/Mandelbrot_set
    """ 
    x_current, y_current = 0, 0
    n = 0
    while not is_unbound(x_current, y_current , limit=2) and n < nb_iter:
        x_current, y_current = next_iter(x_current, y_current, x, y) # iterating
        n += 1
     
    # If the x, y coordinate remained bound, return True, otherwise False.
    return n == nb_iter
    