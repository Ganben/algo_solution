# -*- coding: utf-8 -*-
# ganben
# use set, list sort, assertCountEqual

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
        res = set([])
        d = {}  # num: counts
        st = []
        for e in nums:
            if d.get(e, 0) == 0: # if matched, add this
                d[e] = 1
            else:
                d[e] += 1
        print('%s'%d)
        st2 = set([])

        for k,v in d.items():
            if k not in st:
                st.append(k)

            if v >= 3 and k == 0:
                res.add((0, 0, 0))
                st2.add((0,0))
            elif v >= 2:
                if d.get((0-k-k)) >= 1:
                    l = [k, k, 0-k-k]
                    l.sort()
                    res.add((l[0], l[1], l[2]))
                    st2.add((k, k))
            else:
                pass
        st.sort() # use internal sort


        for i in range(len(st)):
            v = st.pop(0)
            
            stt = st.copy()
            # stt.remove(v)
            for vv in stt:
                if v == vv:
                    break # already exclude in set copy
                elif v < vv and ((v, vv) not in st2):
                    if d.get(0-v-vv, 0) >= 1 and v != 0-v-vv and vv != 0-v-vv:
                        l = [v, vv, 0-v-vv]
                        l.sort()
                        res.add((l[0], l[1], l[2]))
                        st2.add((v, vv))
                        # stt.remove(v)
                        # stt.remove(vv) # not allowed
        print('%s'%res)
        return [[v1, v2, v3] for v1,v2,v3 in res ]





class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
                Solution().threeSum([-1, 0, 1, 2, -1, -4]),
                [
                    [-1, 0, 1],
                    [-1, -1, 2]
                ]     
        )