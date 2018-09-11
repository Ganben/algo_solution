# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        plist = []
        vlist = []
        lnlist = []
        for i in lists:
            lnlist.append(i)
            # vlist.append(i.val)
            while i.next is not None:
                i = i.next
                lnlist.append(i)
        
        for i in range(len(lnlist)):
            plist.append((lnlist[i].val, i))
        plist.sort()
        
        for i in range(len(plist) - 1):
            lnlist[plist[i][1]].next = lnlist[plist[i+1][1]]
        
        return lnlist[0]
class Test(unittest.TestCase):
    def test1(self):
        n3 = ListNode(5)
        n6 = ListNode(4)
        n2 = ListNode(4)
        n2.next = n3
        n1 = ListNode(1)
        n1.next = n2
        n4 = ListNode(1)
        n5 = ListNode(3)
        n7 = ListNode(2)
        n8 = ListNode(6)
        n4.next = n5
        n5.next = n6
        n7.next = n8

        i = [
            n1,
            n4,
            n7
        ]
        r = Solution().mergeKLists(i)
        while r.next is not None:
            print(r.val)
            r = r.next

        self.assertIsNotNone(
            Solution().mergeKLists(i)
        )