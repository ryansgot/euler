#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 001 of the Euler Project
# Assumes: Python 2.7
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# used to filter the numbers in the range
def is_multiple_of_3_or_5(num):
    return 0 == num % 3 or 0 == num % 5

# sum maintains state through loop
sum = 0
for num in filter(is_multiple_of_3_or_5, range(1, 1000)):
    sum += num

# print the sume
print str(sum)