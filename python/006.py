#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 006 of the Euler Project
# Assumes: Python 2.7
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# the sum of the squares of the integers between [low, high)
def sum_of_squares(low, high):
    return sum([x * x for x in range(low, high)])

# the square of the sum of numbers between low and high [low, high)
def square_of_sum(low, high):
    sum_to_square = sum([x for x in range(low, high)])
    return sum_to_square * sum_to_square

print str(square_of_sum(1, 101) - sum_of_squares(1, 101))
