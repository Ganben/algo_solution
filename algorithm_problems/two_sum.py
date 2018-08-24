# -*- coding: utf-8 -*-
# ganben
# 

'''
https://leetcode.com/problems/two-sum/description/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

import unittest



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
            i += 1
        
        for i in range(len(nums)):
            c = target - nums[i]
            if m.get(c) != None and m.get(c) != i:
                return [i, m.get(c)]

class Test(unittest.TestCase):
    t = Solution()
    def test_example(self):
        self.assertEqual(
            self.t.twoSum(
                nums = [2, 7, 11, 15],
                target = 9
            ),
            [0, 1]
        )