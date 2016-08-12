#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        p = head
        i = 0
        while p:
            i += 1
            p = p.next

        q = root
        j = 0
        while j < i-n:
            q = q.next
            j += 1

        q.next = q.next.next

        return root.next
