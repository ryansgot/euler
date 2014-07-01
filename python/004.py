#!/usr/bin/python
#
# Author: Ryan Scott
# Purpose: Solve problem 003 of the Euler Project
# Assumes: Python 2.7
#
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

# determines whether a number is a palindrome or not
def is_palindrome(num):
    # split digits of num into a list
    in_num = num
    digit_list = []
    while in_num > 0:
        digit_list.append(in_num % 10)
        in_num /= 10
    
    # ensure the digits at the two ends of the list are equal
    while len(digit_list) > 1:
        if digit_list.pop(0) != digit_list.pop(len(digit_list) - 1):
            return False
    return True

# determines whether a number is a product of two three digit numbers
def is_product_of_two_3_digit_numbers(num):
    one_divisor = 999
    while one_divisor >= 100:
        if 0 == num % one_divisor:
            another_divisor = num / one_divisor
            if 100 <= another_divisor and 1000 > another_divisor:
                return True
        one_divisor -= 1
    return False
    
#print "is_product_of_two_3_digit_numbers(1): " + str(is_product_of_two_3_digit_numbers(1))
#print "is_product_of_two_3_digit_numbers(100000): " + str(is_product_of_two_3_digit_numbers(100000))

# maintain state of loop
largest = 0
num = 999 * 999
lowest = 100 * 100
while num >= lowest:
    if is_palindrome(num) and is_product_of_two_3_digit_numbers(num):
        largest = num
        break
    num -= 1

print str(largest)