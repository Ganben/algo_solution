# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/valid-parentheses/description/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Node:
    def __init__(self, v, m):
        self.v = v
        self.m = m

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n1 = Node('r', None)
        f = [n1]
        oset = set(['(', '[', '{'])
        cset = set([')', ']', '}'])
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in oset:
                f.append(Node(i, f[-1]))
            elif i in cset and f[-1].v == d.get(i):
                f.pop(-1)
        
        if len(f) == 1:
            return True
        else:
            print('%s' % f[-1].v)
            return False
    

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            list(map(Solution().isValid, ["()", "()[]{}", "(]", "([)]", "{[]}"])),
            [True, True, False, False, True]
        )
