# -*- coding: utf-8 -*-
# ganben
# use set, list sort, assertCountEqual

import unittest

'''
https://leetcode.com/problems/3sum-closest/description/
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numsd = [self.abs(i,1) for i in nums]
        m = {}
        for i in range(len(nums)):
            m[numsd[i]] = nums[i]
        numsd.sort()
        return m.get(numsd[0]) + m.get(numsd[1]) + m.get(numsd[2])

    def abs(self, a, b):
        "absolute distance between 2"
        return a - b if a - b >=0 else b - a


        

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().threeSumClosest(
                [-1, 2, 1, -4],
                1
            ),
            2
        )