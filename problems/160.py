#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA

        i = 0
        while p:
            i += 1
            p = p.next
        n = i

        q = headB
        j = 0
        while q:
            j += 1
            q = q.next
        m = j

        if m > n:
            p = headA
            q = headB
            k = 0
            while p and q:
                k += 1

                if k > m-n:
                    if p.val == q.val:
                        return p
                    else:
                        q = q.next
                        p = p.next
                else:
                    q = q.next

            return None
        else:
            p = headA
            q = headB
            k = 0
            while p and q:
                k += 1

                if k > n-m:
                    if p.val == q.val:
                        return p
                    else:
                        q = q.next
                        p = p.next
                else:
                    p = p.next

            return None