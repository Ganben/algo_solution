# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/3sum/description/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        d = {}  # num: counts
        st = set([])
        for e in nums:
            if d.get(e, 0) == 0: # if matched, add this
                d[e] = 1
            else:
                d[e] += 1
        
        for k,v in d:
            if v >= 3 and k == 0:
                res.append([0 , 0, 0])
            elif v >= 2:
                if d.get((0-k-k)) >= 1:
                    res.append([k, k, 0-k-k])
            else:
                st.add(k)
        
        for v in st:
            





class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            list(map(
                Solution().threeSum,
                [-1, 0, 1, 2, -1, -4])),
                [
                    [-1, 0, 1],
                    [-1, -1, 2]
                ]     
        )