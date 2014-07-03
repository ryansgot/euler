#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 009 of the Euler Project
# Assumes: Python 2.7
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from prime import Prime

prime = Prime()
num = 3 # start including 2
sum = 2 # start including 2
while num < 2000000:
    if prime.is_prime(num):
        sum += num
    num += 2    # the only even prime is 2, cuts problem size in half
print str(sum)