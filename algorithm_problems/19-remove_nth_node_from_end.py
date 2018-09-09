# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n >= 1:
            f1 = head
            f = head
            # f2 = f.next
        else:
            f1 = head
            f = head
            # f2 = f

        for i in range(n):
            f = f.next
        
        if f.next is not None:
            f1 = self.removeNthFromEnd(f1.next, n)
        else:
            f1.next = f1.next.next
        
        return head


class Test(unittest.TestCase):
    def test1(self):
        n5 = ListNode(5, None)
        n4 = ListNode(4, n5)
        n3 = ListNode(3, n4)
        n2 = ListNode(2, n3)
        n1 = ListNode(1, n2)
        Solution().removeNthFromEnd(n1, 2)
        self.assertEqual(
            n5,
            n1.next.next.next 
        )