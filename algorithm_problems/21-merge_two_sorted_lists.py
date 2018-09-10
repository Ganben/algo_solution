# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def p(self):
        print('%s' % self.val)
        if self.next is not None:
            
            self.next.p()
        # else:
            

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1.val >= l2.val:
            p1 = l1
            p2 = l2
            rr = l1
        else:
            p1 = l2
            p2 = l1
            rr = l2
        
        while p1.next is not None and p2.next is not None:
            if p1.val <= p2.val and p1.next.val >= p2.val:
                p = p1.next
                p1.next = p2
                p1 = p
            elif p1.val < p2.val and p1.next.val < p2.val:
                p1 = p1.next
            elif p1.val > p2.val and p1.val > p2.next.val:
                p2 = p2.next
            elif p1.val >= p2.val and p1.val <= p2.next.val:
                p = p2.next
                p2.next = p1
                p2 = p
        
        while p1.next is not None or p2.next is not None:
            if p1.next is None and p1.val >= p2.next.val:
                p2 = p2.next
                
            elif p1.next is None and p1.val <= p2.next.val:
                p1.next = p2
                break

            elif p2.next is None and p2.val <= p1.next.val:
                p2.next = p1
                break 

            elif p2.next is None and p2.val >= p1.next.val:
                p1 = p1.next

        return rr

        
class Test(unittest.TestCase):
    def test1(self):
        n4 = ListNode(4)
        nn4 = ListNode(4)
        n2 = ListNode(2)
        n2.next = n4
        nn3 = ListNode(3)
        nn3.next = nn4
        n1 = ListNode(1)
        n1.next = n2
        nn1 = ListNode(1)
        nn1.next = nn3
        n1.p()
        nn1.p()
        r = Solution().mergeTwoLists(n1, nn1)
        
        self.assertIsNotNone(r)
        self.assertIsNone(r.p())
        
        # self.assert