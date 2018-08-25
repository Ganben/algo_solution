# -*- coding: utf-8 -*-
# ganben
# 

'''
https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 != None and l2 != None:
            v = l1.val + l2.val
            if v > 9:
                v -= 10
                if l1.next != None:
                    l1.next.val += 1
                elif l2.next != None:
                    l2.next.val += 1
                else:
                    carrynode = ListNode(1)
                    l1.next = carrynode
            nn = ListNode(v, self.addTwoNumbers(l1.next, l2.next))
            return nn
        elif l1 != None and l2 == None:
            if l1.val > 9:
                l1.val -= 10
                if l1.next != None:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            
            nn = ListNode(x=l1.val, next=self.addTwoNumbers(l1.next, None))
            return nn
            
        elif l1 == None and l2 != None:
            return self.addTwoNumbers(l2, l1)
        
        else:
            return None

        
        

        
class Test(unittest.TestCase):
    i1 = ListNode(3)
    i2 = ListNode(4, i1)
    i3 = ListNode(2, i2)
    i4 = ListNode(4)
    i5 = ListNode(6, i4)
    i6 = ListNode(5, i5)

    t = Solution()
    def test_example(self):
        r = self.t.addTwoNumbers(self.i3, self.i6)
        self.assertEqual(
            r.val,
            7
        )
        self.assertEqual(
            r.next.val,
            0
        )
        self.assertEqual(
            r.next.next.val,
            8
        )
        self.assertIsNone(
            r.next.next.next
        )