# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = min(list(map(len, strs)))
        res = []
        for i in range(l):
            e = strs[0][i]
            flag = False
            for el in strs:
                if el[i] == e:
                    pass
                else:
                    flag = True
            if flag:
                break
            else:
                res.append(e)
        return ''.join(res)

class Test(unittest.TestCase):
    def test1(self):
        
        self.assertEqual(
            list(map(Solution().longestCommonPrefix, 
            [["flower","flow","flight"],["dog","racecar","car"]])),
            ["fl", ""]
        )