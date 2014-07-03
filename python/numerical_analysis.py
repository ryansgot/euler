#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Provide functions that have to do with numerical analysis
# Assumes: Python 2.7
#

import math

# Find the least common multiple of an arbitrary amount of numbers
def lcm(*nums):
    # gcd would require at least one argument
    if 0 == len(nums):
        raise NotEnoughArgumentsException("0 arguments given, lcm algorithm requires at least 1 argument")
    # return early if the length is just one
    if 1 == len(nums):
        return nums[0]
    
    # this is the base case wherein there are only two
    def two_number_lcm(num1, num2):
        return int(math.fabs(num1 * num2) / gcd(num1, num2))
    
    # handle a list implementation of this
    def lcm_list(num_list):
        if 2 < len(num_list):
            return two_number_lcm(num_list[0], lcm_list(num_list[1:]))
        return two_number_lcm(num_list[0], num_list[1])
    
    return lcm_list(list(nums))

# Find the gcd of an arbitrary amount of integers
def gcd(*nums):
    # gcd would require at least one argument
    if 0 == len(nums):
        raise NotEnoughArgumentsException("0 arguments given, gcd algorithm requires at least 1 argument")
    # return early if the length is just one
    if 1 == len(nums):
        return nums[0]
        
    # the two_number_gcd is a necessary special case to find the more generic case
    def two_number_gcd(larger, smaller):
        # swap the larger and smaller number if they happen to be flipped
        if larger < smaller:
            larger, smaller = smaller, larger
        
        # exit early if one of the values was zero (corresponds to a previous invocations remainder being zero)
        if 0 == smaller:
            return larger
        return two_number_gcd(smaller, larger % smaller)
    
    # handle a list implementation of this
    def gcd_list(num_list):
        if 2 < len(num_list):
            return two_number_gcd(num_list[0], gcd_list(num_list[1:]))
        return two_number_gcd(num_list[0], num_list[1])
    
    # make the input into a list and calculate the GCD
    return gcd_list(list(nums))
        
class NotEnoughArgumentsException(Exception):
    def __init__(self, value):
         self.value = value
    def __str__(self):
         return repr(self.value)