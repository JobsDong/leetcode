#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root_odd = ListNode(0)
        odd_head = root_odd
        root_even = ListNode(0)
        even_head = root_even

        p = head
        i = 1
        while p:
            temp = p.next
            if i % 2 == 1:
                odd_head.next = p
                p.next = None
                odd_head = p
            else:
                even_head.next = p
                p.next = None
                even_head = p
            i += 1
            p = temp

        odd_head.next = root_even.next

        return root_odd.next