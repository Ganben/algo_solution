# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/next-permutation/description/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                n1 = nums[i]
            elif i < len(nums) - 1 and i > 0:
                if nums[i] < n1:
                    swap = nums[i]
                    nums[i] = n1
                    nums[i+1] = swap
                    return nums
                else:
                    n1 = nums
                    continue
            elif i == 0:
                return nums[::-1]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().nextPermutation(
                [1,2,3]
            ),
            [1,3,2]
        )
    def test2(self):
        self.assertEqual(
            Solution().nextPermutation(
                [3,2,1]
            ),
            [1,2,3]
        )
    def test3(self):
        self.assertEqual(
            Solution().nextPermutation(
                [1,1,5]
            ),
            [1,5,1]
        )
