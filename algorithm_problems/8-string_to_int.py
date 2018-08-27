# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/string-to-integer-atoi/description/
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = []
        flag = 1
        n_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        m = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        out = 0
        for i in range(len(str)):
            # discard \s
            if str[i] == ' ':
                pass
            elif str[i] == '-':
                flag = -1
            elif str[i] in n_set:
                s.append(m.get(str[i]))
            else:
                break
        rs = s[::-1]
        if len(rs) == 0:
            return 0
        res = 0
        for i in range(len(rs)):
            if res + rs[i] * self.powerten(i) >= 2147483648:
                return flag * 2147483648
            res += rs[i] * self.powerten(i)

        return res * flag
        

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
    t = Solution()
    def test1(self):
        i = "42"
        o = 42
        self.assertEqual(
            self.t.myAtoi(i),
            o
        )

    def test2(self):
        i = "     42"
        o = 42
        self.assertEqual(
            self.t.myAtoi(i),
            o
        )
    
    def test3(self):
        i = "4193 with words"
        o = 4193
        self.assertEqual(
            self.t.myAtoi(i),
            o
        )

    def test4(self):
        i = "words and 987"
        o = 0
        self.assertEqual(
            self.t.myAtoi(i),
            o
        )
    
    def test5(self):
        i = "-91283472332"
        o = -2147483648 # -2^32
        self.assertEqual(
            self.t.myAtoi(i),
            o
        )