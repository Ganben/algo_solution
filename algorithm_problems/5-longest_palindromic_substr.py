# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # center expand method
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i+1)
            l0 = max(l1, l2)
            if l0 > end - start:
                start = i - int((l0 -1) /2)
                end = i + int(l0/2)
        return s[start:end+1]

    def expandAroundCenter(self, s, l, r):
        while (l >= 0 and r < len(s)) and s[l] == s[r] :
            l -= 1
            r += 1
        return r - l -1 

    def longestPalindrome_manacher(self, s):
        # TODO as name
        pass
        

class Test(unittest.TestCase):
    def test1(self):
        t = Solution()
        self.assertEqual(
            t.longestPalindrome("babad"),
            "aba"
        )
    def test2(self):
        t = Solution()
        self.assertEqual(
            t.longestPalindrome("cbbd"),
            "bb"
        )