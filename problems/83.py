#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        p1 = head
        if p1 is None:
            return root.next
        p = p1.next
        if p is None:
            return root.next

        while p:
            if p.val == p1.val:
                p1.next = p.next
            else:
                p1 = p1.next

            p = p.next

        return root.next