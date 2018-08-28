# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/regular-expression-matching/description/
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or 
                    first_match and self.isMatch(s[1:], p))
        
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        

class Test(unittest.TestCase):
    def test1(self):
        s = "aa"
        p = "a"
        t = Solution()
        self.assertEqual(
            t.isMatch(s,p),
            False
        )
    
    def test2(self):
        s = "aa"
        p = "a*"
        t = Solution()
        self.assertEqual(
            t.isMatch(s,p),
            True
        )
    
    def test3(self):
        s = "ab"
        p = ".*"
        t = Solution()
        self.assertEqual(
            t.isMatch(s,p),
            True
        )

    def test4(self):
        s = "aab"
        p = "c*a*b"
        t = Solution()
        self.assertEqual(
            t.isMatch(s,p),
            True
        )

    def test5(self):
        s = "mississippi"
        p = "mis*is*p*."
        t = Solution()
        self.assertEqual(
            t.isMatch(s,p),
            False
        )