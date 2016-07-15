#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2

        if p1 or p2:
            parent = p3 = ListNode(0)
        else:
            parent = p3 = None

        while p1 and p2:
            if p1.val <= p2.val:
                p3.val = p1.val
                p1 = p1.next
            else:
                p3.val = p2.val
                p2 = p2.next

            p3.next = ListNode(0)
            p3 = p3.next

        while p1:
            p3.val = p1.val

            p1 = p1.next
            if p1:
                p3.next = ListNode(0)
                p3 = p3.next

        while p2:
            p3.val = p2.val
            p2 = p2.next
            if p2:
                p3.next = ListNode(0)
                p3 = p3.next

        return parent
