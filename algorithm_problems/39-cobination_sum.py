# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/combination-sum/description/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        min_cand = min(candidates)
        max_cand = max(candidates)
        r = []
        for e in candidates:
            v = target
            v -= e
            
            if v < min_cand:
                continue
            else:
                if self.combinationSum(candidates, v):
                     r.append(self.listadd(self.combinationSum(candidates,v), e))
                else:
                    continue
        
        return r

    def listadd(self, vec1, v1):
        for e in vec1:
            e.append(v1)
        return vec1        


class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().combinationSum(
                [2,3,6,7],
                7
            ),
            [
                [7],
                [2,2,3]
            ]
        )
    def test2(self):
        self.assertCountEqual(
            Solution().combinationSum(
                [2,3,5],
                8
            ),
            [
                [2,2,2,2],
                [2,3,3],
                [3,5]
            ]
        )