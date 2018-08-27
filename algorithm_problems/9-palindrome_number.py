# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/palindrome-number/description/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digit = 0
        n = 1
        while n <= x:
            n = n * 10
            digit += 1
        print(digit)
        n = x
        d=[]
        for i in range(digit):
            j = int(n/self.powerten(digit-i-1))
            d.append(j)
            n -= j*self.powerten(digit-i-1)
        rd = d[::-1]
        for i in range(len(rd)):
            if rd[i] != d[i]:
                return False
        return True
        
    def powerten(self, n):
        if n == 0:
            return 1
        elif n >= 1:
            r = 1
            for i in range(n):
                r = 10 * r
            return r
        else:
            return 0


class Test(unittest.TestCase):
    def test1(self):
        t = Solution()
        self.assertEqual(
            t.isPalindrome(121),
            True
        )
        self.assertEqual(
            t.isPalindrome(-121),
            False
        )
        self.assertEqual(
            t.isPalindrome(10),
            False
        )