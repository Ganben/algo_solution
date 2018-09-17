# -*- coding: utf-8 -*-
# ganben
#

import unittest
import math
'''
https://leetcode.com/problems/count-and-say/description/
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        d = []
        for i in range(n):
            # s = next_s
            
            if i == 0:
                
                s = '1'
                # d.append([1,0])
            
            else:
                d = []
                for el in s:
                    if len(d) == 0:
                        d.append([int(el), 1])
                    elif d[-1][0] == int(el):
                        d[-1][1] += 1 
                    else:
                        d.append([int(el), 1])
                n_s = []
                print(d)
                for ii in range(len(d)):
                    
                    n_s.append('%s%s'%(d[ii][1],d[ii][0]))
                
                s = ''.join(n_s)
                
                
            
        if len(s) == 1:
            return '1'
        else:
            res = ''
            for e in d:
                res += '%s%s' % (e[1], e[0])
        
            return res


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().countAndSay(1),
            "1"
        )
    def test2(self):
        self.assertEqual(
            Solution().countAndSay(4),
            "1211"
        )