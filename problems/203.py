4#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        p1 = root
        p = head

        while p:
            if p.val == val:
                p1.next = p.next
                p = p1.next
            else:
                p1 = p1.next
                p = p.next

        return root.next