# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/integer-to-roman/description/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        r = ''
        # M
        if num > 1000:
            n = int(num/1000)
            for i in range(n):
                r = ''.join([r, d.get(1000)])
        # C - D
        num2 = num % 1000
        if num2 > 100:
            if num2 >= 900:
                r = ''.join([r, "CM"])
            elif num2 >= 500:
                r = ''.join([r, "D"])
                for i in range(int((num2-500)/100)):
                    r = ''.join([r, "C"])
            elif num2 >= 400:
                r = ''.join([r, "CD"])
            else:
                for i in range(int(num2/100)):
                    r = ''.join([r, "C"])
        # L - X
        num3 = num2 % 100
        if num3 > 10:
            if num3 >= 90:
                r = ''.join([r, "XC"])
            elif num3 >= 50:
                r = ''.join([r, "L"])
                for i in range(int((num3-500)/10)):
                    r = ''.join([r, "X"])
            elif num3 >= 40:
                r = ''.join([r, "XL"])
            else:
                for i in range(int(num3/10)):
                    r = ''.join([r, "X"])
        
        # I - V
        
        num4 = num3 % 10
        if num4 != 0:
            if num4 == 9:
                r = ''.join([r, "IX"])
            elif num4 >= 5:
                r = ''.join([r, "V"])
                for i in range(num4-5):
                    r = ''.join([r, "I"])
            elif num4 == 4:
                r = ''.join([r, "IV"])
            else:
                for i in range(num4):
                    r = ''.join([r, "I"])
        
        return r

class Test(unittest.TestCase):
    def test1(self):
        t = Solution()
        i = 3
        o = "III"
        self.assertEqual(
            t.intToRoman(i),
            o
        )
    def test2(self):
        t = Solution()
        i = 4
        o = "IV"
        self.assertEqual(
            t.intToRoman(i),
            o
        )
    def test3(self):
        t = Solution()
        i = 9
        o = "IX"
        self.assertEqual(
            t.intToRoman(i),
            o
        )
    def test4(self):
        self.assertEqual(
            list(map(Solution().intToRoman, [58, 1994])),
            ["LVIII", "MCMXCIV"]
        )
