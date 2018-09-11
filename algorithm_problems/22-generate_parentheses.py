# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
# i use graph and render it from start node
class Node:
    def __init__(self, v):
        self.n = v
        self.edges = []
        self.child = []
    @property
    def generated(self):
        r = []
        for i in self.child:
            r.append(i.generated)
        if self.n != 0:
            return '(%s)' % ''.join(r)
        else:
            return '%s' % ''.join(r)




class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        # n1.edges.append(self)


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        # s = n + 1
        def backtrack(nodes):
            if nodes == 1:
                list1 = []
                list1.append(Edge(0, 1))
                return [list1]
            elif nodes >= 2:
                     
                eg1 = backtrack(nodes -1)
                eg2 = []
                for i in range(nodes):
                    eg2.append(Edge(i, nodes))
                return self.vectormult(eg1, eg2)
        e = backtrack(n)
        for i in e:
            res.append(self.render(i))
        return res
    
    def render(self, edgelist):
        ns = []

        for i in range(edgelist[-1].n2 + 1):
            # print(i)
            ns.append(Node(i))

        for i in edgelist:
            print('edge%s,%s' % (i.n1, i.n2))
            ns[i.n1].child.append(ns[i.n2])   
        
        return ns[0].generated

    def vectormult(self, v1, v2):
        # v1 = v.copy()
        # v2 = vv.copy()
        r = []
        for i in range(len(v1)):
            for ii in range(i,len(v2)):
                print('V%sV%s' % (i, ii))
                r.append(v1[i] + [v2[ii]])
        return r

class Test1(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            Solution().generateParenthesis(
                3
            ),
            [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
            ]
        )
