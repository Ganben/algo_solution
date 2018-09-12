# -*- coding: utf-8 -*-
# ganben
#

import unittest

'''
https://leetcode.com/problems/reverse-nodes-in-k-group/description/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        f = 0
        pcache = []
        tail = None
        while head is not None:
            
            pcache.append(head)
            if f % k == k-1:
                if f == k-1:
                    r = head # the first xx
                # finish 1st circule
                nexthead = head.next
                # swap cached 
                for i in range(k-1):
                    pcache[i+1].next = pcache[i]
                pcache[0].next = tail
                # clearing
                pcache.clear()
                head = nexthead
                f += 1
                continue
            
            if f % k == 0:
                pp = head
                # determine next tail
                for i in range(2*k - 2):
                    if i == k -1:
                        tail1 = pp.next # even if it is None
                    if i == 2*k - 2:
                        tail = pp.next
                    if pp.next is None:
                        tail = tail1
                        print('beak tail on %s' % pp.val)
                        break
                    pp = pp.next
            
            # step forward
            f += 1
            head = head.next
                
        return r

        
class Test(unittest.TestCase):
    def test1(self):
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        self.assertEqual(
            Solution().reverseKGroup(n1, 3),
            n3
        )