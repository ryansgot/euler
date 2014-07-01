#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Provide Prime number class/methods to those that import
# Assumes: Python 2.7
#

import math

# Classes #
class Prime:
    def __init__(self):
        self.primes = [2]   # hold the minimal number of primes necessary to check whether a number is prime via is_prime method
        self.highest_recorded_prime = 2 # starting prime
    
    def __str__(self):
        return str(self.primes)
    
    # return true if a number is prime
    def is_prime(self, num):
        # be strict about the definition of a prime being an integer greater than 1
        if type(num) != int:
            raise PrimeNumberException("Cannot check whether input: " + str(num) + " is prime. It is of type: " + str(type(num)))
        
        # early exit for base case, 2 and below
        if 2 > num:
            return False
        elif 2 == num:
            return True
        
        # check whether all recorded primes between 2 and the square root (inclusive) of the number checked are 
        highest_necessary_check = int(math.ceil(math.sqrt(num)))
        
        # add any primes that are not already in the list of primes which would be necessary to check
        if highest_necessary_check > self.highest_recorded_prime:
            self.set_primes_to_threshold(highest_necessary_check + 1)
        
        # check whether any primes in the region that are necessary to check divide the number
        for possible_divisor in [x for x in self.primes if x <= highest_necessary_check]:
            if 0 == num % possible_divisor:
                return False
        
        return True
    
    # get the primes to the threshold (non-inclusive)
    def get_primes_to_threshold(self, num):
        # the base case is to get the primes to the threshold when all of those primes are already recorded
        if num <= self.highest_recorded_prime:
            return [x for x in self.primes if x < num]
        
        # if not the primes must be set to the threshold (non-inclusive)
        self.set_primes_to_threshold(num)
        return self.primes
    
    # append all primes up to num (non-inclusive). This is the only way you can safely append
    # to the primes list because it depends upon the primes being listed in increasing order.
    def set_primes_to_threshold(self, num):
        # the base case is when the primes already exist, so do nothing in that case
        if num <= self.highest_recorded_prime:
            return
        
        # otherwise, the primes must be filled in
        for possible_prime in range(self.highest_recorded_prime + 1, num):
            if self.is_prime(possible_prime):
                self.primes.append(possible_prime)
                if self.highest_recorded_prime < possible_prime:
                    self.highest_recorded_prime = possible_prime
        
class PrimeNumberException(Exception):
    def __init__(self, value):
         self.value = value
    def __str__(self):
         return repr(self.value)