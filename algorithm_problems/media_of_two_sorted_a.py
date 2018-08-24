# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        
        imin, imax, half_len = 0, m, int((m + n + 1)/2)
        while imin <= imax:
            i = int( (imin + imax)/2)
            j = half_len -i
            if i < m and nums2[j-1] > nums1[i]:
                # increase i
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # decrease i
                imax = i - 1

            else:
                # i is good
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return float(max_of_left)
            
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0

class Test(unittest.TestCase):

    def test1(self):
        n1 = [1, 3]
        n2 = [2]
        t = Solution()
        self.assertEqual(
            t.findMedianSortedArrays(n1, n2),
            2.0
        )
    def test2(self):
        n1 = [1, 2]
        n2 = [3, 4]
        t = Solution()
        self.assertEqual(
            t.findMedianSortedArrays(n1, n2),
            2.5
        )