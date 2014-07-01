#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 003 of the Euler Project
# Assumes: Python 2.7
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from prime import Prime
import math

num = 600851475143

# keep track of state through loop
largest_prime_divisor = 0
prime = Prime()
for possible_divisor in range(2, int(math.ceil(math.sqrt(num)))):
    if 0 == num % possible_divisor and prime.is_prime(possible_divisor):
        if possible_divisor > largest_prime_divisor:
            largest_prime_divisor = possible_divisor

print str(largest_prime_divisor)