#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 007 of the Euler Project
# Assumes: Python 2.7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from prime import Prime

prime = Prime()
prime_count = 6 # given by problem
num = 14        # next number to try
while True:
    if prime.is_prime(num):
        prime_count += 1
    if 10001 == prime_count:
        break
    num += 1

print str(num - 1)