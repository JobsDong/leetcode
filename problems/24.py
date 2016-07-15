#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = parent = ListNode(0)
        root.next = parent.next = head

        if not parent.next:
            return None
        p1 = parent.next
        p2 = p1.next

        while p1 and p2:
            p1.next = p2.next
            p2.next = p1
            parent.next = p2

            #
            parent = p1
            p1 = p1.next if p1 else None
            p2 = p1.next if p1 else None

        return root.next