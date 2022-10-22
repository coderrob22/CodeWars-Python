#Write a function which calculates the average of the numbers in a given list.

#Note: Empty arrays should return 0.

import numpy
def find_average(numbers):
    return numpy.average(numbers)

or


def find_average(array):
    return sum(array) / len(array) if array else 0


or

from statistics import mean as find_average