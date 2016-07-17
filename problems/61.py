#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        root = p = ListNode(0)
        p.next = head

        i = 0
        while p.next:
            i += 1
            p = p.next

        tail = p
        n = i

        k %= n

        # -------
        p = root
        j = 0
        while p:
            if j == n-k:
                break
            j += 1
            p = p.next

        re_p = p

        tail.next = head
        root.next = re_p.next
        re_p.next = None

        return root.next
