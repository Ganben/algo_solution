# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/reverse-integer/description/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            flag = 1
        else:
            x = -x
            flag = -1

        s = str(x)
        # h = len(s)
        return int(s[::-1]) * flag

    
class Test(unittest.TestCase):
    t = Solution()
    def test1(self):
        
        i = 123
        o = 321
        self.assertEqual(
            self.t.reverse(i),
            o
        )
    def test2(self):
        i = -123
        o = -321
        self.assertEqual(
            self.t.reverse(i),
            o
        )
    def test3(self):
        i = 120
        o = 21
        self.assertEqual(
            self.t.reverse(i),
            o
        )