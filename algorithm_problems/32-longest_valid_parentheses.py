# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/longest-valid-parentheses/description/
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
class PNode:
    def __init__(self):
        self.closure = 0
        self.child = []
        self.parent = None
        self.brother = 0
    @property
    def isValid(self):
        if len(self.child) == 0 and self.closure == 1:
            return True
        elif len(self.child) > 0 and self.closure == 1:
            for e in self.child:
                if not e.isValid:
                    return False
            return True
        elif self.closure == 0:
            return False
        else:
            return False
    
    @property
    def stringfy(self):
        # return longest valid node:
        subs = []
        if True:
            for e in self.child:
                if e.isValid:
                    subs.append(e.stringfy)
                else:
                    pass
            if self.isValid:
                return '(%s)' % ''.join(subs)
            else:
                return ''.join(subs)


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # active_nodes = []
        lastnode = None
        longest = 0
        for c in s:
            if c == '(' and lastnode is None:
                # new a node
                n = PNode()
                # active_nodes.append(n)
                lastnode = n
            elif c == '(' and lastnode is None:
                continue
            elif c == ')' and lastnode is not None and lastnode.closure == 0:
                lastnode.closure = 1
                if lastnode.isValid and lastnode.parent is None:
                    # report length;
                    l = len(lastnode.stringfy) + lastnode.brother
                    
                    if longest < l:
                        longest = l
                    else:
                        pass
                elif lastnode.isValid and lastnode.parent is not None:
                    l = len(lastnode.stringfy) + lastnode.brother
                    if longest < l:
                        longest = l
                    else:
                        pass
                    lastnode = lastnode.parent
                else:
                    lastnode = None

            elif c == '(' and lastnode is not None and lastnode.closure == 0:
                n = PNode()
                n.parent = lastnode
                lastnode.child.append(n)
                lastnode = n
            elif c == '(' and lastnode is not None and lastnode.closure == 1:
                if lastnode.isValid and lastnode.parent is not None:
                    n = PNode()
                    lastnode.parent.child.append(n)
                    n.parent = lastnode.parent
                    lastnode = n
                elif lastnode.isValid and lastnode.parent is None:
                    n = PNode()
                    n.brother =  len(lastnode.stringfy) + lastnode.brother
                    lastnode = n
                elif not lastnode.isValid:
                    n = PNode()
                    lastnode = n
                else:
                    n = PNode()
                    lastnode = n
            elif c == ')' and lastnode is not None and lastnode.closure == 1:
                if lastnode.isValid and lastnode.parent is not None and lastnode.parent.closure == 0:
                    lastnode = lastnode.parent
                    lastnode.closure == 1
                    if lastnode.isValid:
                        l = len(lastnode.stringfy) + lastnode.brother
                        if longest < l:
                            longest = l
                        else:
                            pass
                    else:
                        lastnode = None
                elif lastnode.isValid and lastnode.parent is None:
                    # a broken point
                    lastnode = None
                    continue
            elif c == ')' and lastnode is None:
                continue
            else:
                lastnode = None
                
        return longest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().longestValidParentheses(
                "(()"
            ),
            2
        )
    
    def test2(self):
        self.assertEqual(
            list(map(
                Solution().longestValidParentheses,
                [")()())", "((())())()(())"]
            )),
            [4, 14]
        )
if __name__ == "__main__":
    s = Solution().longestValidParentheses("(())()()")
    print('%s' % s)