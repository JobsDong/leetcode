#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        # num
        p = head
        i = 0
        while p:
            i += 1
            p = p.next

        # mid reverse mid ~ n
        mid = i/2-1 if i % 2 ==0 else i/2
        j = 0
        q = head
        r = head
        while q and q.next:
            if j < mid:
                q = q.next
                j += 1
            elif j == mid:
                r = q
                q = q.next
                j += 1
            else:
                t = q.next
                q.next = q.next.next
                t.next = r.next
                r.next = t

        # swap
        p = r
        q = head
        while p.next and p != q:
            next_q = q.next
            t = p.next
            p.next = p.next.next
            t.next = q.next
            q.next = t

            q = next_q
