#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        p = root
        q = root


        while q and q.next:
            if q.next.val < x:
                if p == q:
                    q = q.next
                    p = p.next
                else:
                    temp = q.next
                    q.next = q.next.next

                    temp.next = p.next
                    p.next = temp
                    p = p.next
            else:
                q = q.next
        return root.next
