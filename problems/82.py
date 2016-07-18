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

        p1_before = root
        p1 = head
        if p1 is None:
            return root.next
        p = p1.next

        if p is None:
            return root.next

        is_duplicate = False

        while p:
            if p1.val == p.val:
                if is_duplicate:
                    p = p.next
                else:
                    is_duplicate = True
            else:
                if is_duplicate:
                    p1_before.next = p
                    p1 = p
                    p = p.next
                    is_duplicate = False
                else:
                    p1_before = p1_before.next
                    p1 = p1.next
                    p = p.next

        if is_duplicate:
            p1_before.next = None

        return root.next