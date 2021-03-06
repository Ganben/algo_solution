# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/combination-sum-ii/description/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = candidates.sort()
        cands = candidates.copy()
        b = target
        ress = []
        for i in range(len(candidates)):
            #cands = candidates
            bm = cands.pop()
            if b > bm or b-bm < min(cands):
                res = self.combinationSum2(cands, b-bm)
                if len(res)>0:
                    res.append(bm)
                else:
                    res = []
            elif b == bm:
                res = [bm]
            
            else:
                res = []
            
            if len(res) > 0:
                ress.append(res)
            else:
                continue
        
        return ress


class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().combinationSum2(
            [10,1,2,7,6,1,5],
            8
          ),
          [
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
        )

    def test2(self):
        self.assertCountEqual(
            Solution().combinationSum2(
            [2,5,2,1,2],
            5
          ),
            [
  [1,2,2],
  [5]
]
        )