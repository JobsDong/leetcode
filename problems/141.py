#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p = head
        if head is not None:
            q = head.next
        else:
            return False

        while p and q:
            if p == q:
                return True

            p = p.next
            if q.next is not None:
                q = q.next.next
            else:
                return False

        return False
