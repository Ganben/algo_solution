# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/swap-nodes-in-pairs/description/
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        if head.next is not None:
            r = head.next
        else:
            return None
        while head.next:
            if i % 2 == 0:
                if head.next.next:
                    p = head.next
                    head.next = p.next.next
                    p.next = head
                else:
                    p = head.next
                    head.next = None
                    p.next = head
            else:
                pass
            i += 1
        
        return r

class Test(unittest.TestCase):
    def test1(self):
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n1.next = n2
        n2.next = n3
        n3.next = n4

        self.assertEqual(
            Solution().swapPairs(
                n1
            ),
            n2
        )