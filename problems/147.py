#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        p = root

        while p.next:
            # optimize
            if p.val < p.next.val:
                p = p.next
                continue

            pos = root
            while pos.next != p.next and pos.next.val < p.next.val:
                pos = pos.next

            if pos.next == p.next:
                p = p.next
            else:
                temp = p.next
                p.next = temp.next

                temp.next = pos.next
                pos.next = temp

        return root.next




