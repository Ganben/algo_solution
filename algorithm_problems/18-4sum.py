# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/4sum/description/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for ii in range(len(nums)-1, i+2, -1):
                if ii < len(nums)-1 and nums[ii] == nums[ii+1]:
                    continue
                f = i + 1
                iif = ii - 1
                while True:
                    sums = nums[i] + nums[f] + nums[iif] + nums[ii]
                    if iif <= f:
                        break
                    elif sums == target:
                        res.append([nums[i], nums[f], nums[iif], nums[ii]])
                        iif -= 1
                        while 0 < iif < len(nums)-1 and nums[iif+1] == nums[iif]:
                            iif -= 1
                        f += 1
                        while len(nums) - 1 > f > 0 and nums[f] == nums[f-1]:
                            f += 1
                    elif sums > target:
                        iif -= 1
                    elif sums < target:
                        f += 1
        
        return res

class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().fourSum(
                [1, 0, -1, 0, -2, 2],
                0
            ),
            [
                [-1,  0, 0, 1],
                [-2, -1, 1, 2],
                [-2,  0, 0, 2]
            ]
        )
