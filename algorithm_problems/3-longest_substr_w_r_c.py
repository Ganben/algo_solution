# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        r = []
        f = []
        flag = 0
        flag2 = 0
        for i in range(len(s)):
            if m.get(s[i]) == None:
                
                m[s[i]] = i
                r.append(s[i])
            else:
                d = i - m.get(s[i])
                print('d=%s' %d)
                r.append(s[i])
                r = r[-d::]
                m[s[i]] = i
            
            f.append(len(r))
            print(' %s' % r)
            

        return max(f)



class Test(unittest.TestCase):
    t = Solution()
    s = "abcabcbb"
    def test_example(self):
        self.assertEqual(
            self.t.lengthOfLongestSubstring(self.s),
            3
        )
    def test2(self):
        self.assertEqual(
            self.t.lengthOfLongestSubstring("bbbbbbbbb"),
            1
        )
    def test3(self):
        self.assertEqual(
            self.t.lengthOfLongestSubstring("pwwkew"),
            3
        )