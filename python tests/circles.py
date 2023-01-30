from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError('The radius of the circle should not be negative.')
    if type(r) not in [int, float]:
        raise TypeError('The radius should be an int or float')
    return pi*(r**2)
