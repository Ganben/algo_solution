# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        delta = 0
        step = 0
        ptr = 0
        result = [-1, -1]
        for i in range(int(math.log(len(nums), 2))+3):
            d = target - nums[ptr]
            if d < 0:
                #modify step
                step = int(len(nums)/pow(2,i+1))
                if step < 1:
                    step = 1
                delta = d
                ptr -= step
            elif d > 0:
                #modify step
                step = int(len(nums)/pow(2, i+1))
                if step == 0:
                    step = 1
                delta = d
                ptr += step
                
            elif d == 0 and result[0] == -1:
                # 4 cases: left end, middle and right end;
                if ptr == 0:
                    result[0] = ptr
                    continue
                elif ptr > 0 and nums[ptr - 1] != target:
                    result[0] = ptr
                    continue
                    # not change ptr
                else:
                    
                # not left end, step decide
                    step = int(len(nums)/pow(2,i+3))
                    if step == 0:
                        step = 1
                    delta = 0
                    ptr -= step
                
                
            elif d == 0 and result[0] != -1:
                # find end
                if ptr == len(nums) -1:
                    result[1] = ptr
                    break
                elif ptr < len(nums) - 1 and nums[ptr+1] != target:
                    result[1] = ptr
                    break
                
                #not right end, step dicide
                step = int(len(nums)/pow(2,i+3))
                if step < 1:
                    step = 1
                delta = 0
                ptr += step
            else:
                ptr += 1
            
        return result

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().searchRange(
                [5,7,7,8,8,10],
                8
            ),
            [3,4]
        )
    def test2(self):
        self.assertEqual(
            Solution().searchRange(
                [5,7,7,8,8,10],
                6
            ),
            [-1,-1]
        )