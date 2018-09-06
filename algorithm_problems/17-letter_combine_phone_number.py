# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
1 2abc 3def 
4 ghi 5jkt 6mon
7pqrs 8tuv 9wxyz

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        for i in range(len(digits)):
            res.append(d.get(digits[i]))
        r = []
        for a in res:
            r = self.vproduct(r, a)

        return r
    
    def vproduct(self, ar1, ar2):
        res = []
        if len(ar1) == 0 and len(ar2) >0:
            return ar2
        elif len(ar1) > 0 and len(ar2) >0:
            for e1 in ar1:
                for e2 in ar2:
                    res.append(''.join((e1, e2)))
        return res



class Test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        )