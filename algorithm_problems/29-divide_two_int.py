# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/divide-two-integers/description/
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend >= 0 and divisor > 0:
            f = 1
        elif dividend <0 and divisor > 0:
            dividend = 0 - dividend
            f = -1
        elif dividend >=0 and divisor < 0:
            divisor = 0 - divisor
            f = -1
        elif dividend <0 and divisor < 0:
            dividend = 0 - dividend
            divisor = 0 - divisor
            f = 1
        else:
            raise ValueError('no 0 div')
        
        r = 0
        while dividend >= divisor:
            r += 1
            dividend -= divisor
            # if r == pow(2, 31) and f == -1:
            #     break
            # elif r == pow(2, 31) -1 and f == 1:
            #     break
        
        return r if f == 1 else 0 - r


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().divide(7, -3),
            -2
        )
    def test2(self):
        self.assertEqual(
            Solution().divide(10, 3),
            3
        )