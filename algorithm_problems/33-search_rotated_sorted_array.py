# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = -1
        
        ptr = 0
        for i in range(int(math.log(len(nums), 2)) + 1):
            if nums[ptr] == target:
                r = ptr
                break
            elif nums[ptr+1] == target:
                r = ptr + 1
                break
            
            # a while loop for O(logN)
            delta = int(len(nums) / pow(2, i+1))
            if delta == 0:
                delta = 1
                
            if nums[ptr] < target:
                ptr -= delta
                if ptr < 0:
                    ptr += len(nums)
            else:
                ptr += delta
                if ptr>len(nums)-2:
                    ptr -= len(nums)
                elif ptr==len(nums)-1:
                    if nums[ptr] == target:
                        r = ptr
                        break
                    else:
                        ptr = 0




        return r

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().search(
                [4,5,6,7,0,1,2],
                0
            ),
            4
        )

    def test2(self):
        self.assertEqual(
            Solution().search(
                [4,5,6,7,0,1,2],
                3
            ),
            -1
        )