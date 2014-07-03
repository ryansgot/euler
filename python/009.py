#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 009 of the Euler Project
# Assumes: Python 2.7
# Bad:     takes 34266 passes through the inner while loop to complete.
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# return true if the input is a pythagorean triple
def is_pythagorean_triple(adj, opp, hyp):
    return hyp * hyp == adj * adj + opp * opp

# monitor state of loops
adj = None
opp = 332   # A good starting point for the algorithm that allows the 
hyp = 334   # algorithm to use only sides that could actually be triangles
found = False

# loop until the one pythagorean triple (as mentioned in the problem) is found
while hyp <= 998:
    while opp < hyp:
        adj = 1000 - hyp - opp  # ensures that the sume of the lengths is always 1000
        if is_pythagorean_triple(adj, opp, hyp):
            found = True
            break
        opp += 1
    if found:
        break
    opp = 1
    hyp += 1

print str(adj * opp * hyp)