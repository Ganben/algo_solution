# -*- coding: utf-8 -*-
# ganben
# 
import unittest

'''
https://leetcode.com/problems/zigzag-conversion/description/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []
        for i in range(numRows):
            row = []
            res.append(row)
        flag = 1
        for i in range(len(s)):
            # n = int(( i + 1 ) / numRows)
            if flag == 1:
                mo = ( i + 1 ) % numRows
            else:
                mo = i % (numRows -1)
            if mo != 0 and flag == 1:
                res[mo-1].append(s[i])
            elif mo ==0 and flag == 1:
                res[mo-1].append(s[i])
                flag += 1
            elif mo != 0 and flag % 2 == 0:
                res[-1-mo].append(s[i])
            elif mo == 0 and flag % 2 == 0:
                res[0].append(s[i])
                flag += 1
            elif mo != 0 and flag % 2 == 1:
                res[mo].append(s[i])
            elif mo == 0 and flag % 2 == 1:
                res[-1].append(s[i])
                flag += 1
            else:
                pass
            
            print('i,mo,flag=%s,%s,%s' % (i, mo, flag))
        
        r = []
        for e in res:
            print(e)
            for el in e:
                r.append(el)

        
        return ''.join(r)






        


class Test(unittest.TestCase):
    def test1(self):
        t = Solution()
        s = "PAYPALISHIRING"
        numRows = 3
        self.assertEqual(
            t.convert(s, numRows),
            "PAHNAPLSIIGYIR"
        )
    def test2(self):
        t = Solution()
        s = "PAYPALISHIRING"
        numRows = 4
        self.assertEqual(
            t.convert(s, numRows),
            "PINALSIGYAHRPI"
        )