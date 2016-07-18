#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head

        root2 = ListNode(0)
        f_0 = None
        f_1 = root
        f_2 = None

        p = root

        i = 0
        while p:
            temp = p.next
            if i == m-1:
                f_1 = p

            if i == m:
                f_0 = p
                root2.next = p
                p.next = None

            if m < i <= n:
                # add to root2
                p.next = root2.next
                root2.next = p

            if i == n+1:
                f_2 = p
                break

            p = temp
            i += 1

        f_1.next = root2.next
        f_0.next = f_2

        return root.next