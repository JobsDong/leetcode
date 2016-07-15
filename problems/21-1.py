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

        parent = p3 = ListNode(0)

        while True:
            if p1 is None:
                p3.next = p2
                break
            elif p2 is None:
                p3.next = p1
                break
            else:
                if p1.val <= p2.val:
                    p3.next = p1
                    p1 = p1.next
                    p3 = p3.next
                else:
                    p3.next = p2
                    p2 = p2.next
                    p3 = p3.next

        return parent.next
