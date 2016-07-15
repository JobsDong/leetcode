#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry = 0
        parent = ListNode(0)
        p3 = parent

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            p3.val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) / 10

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            if p1 or p2:
                p3.next = ListNode(0)
                p3 = p3.next

        if carry > 0:
            p3.next = ListNode(carry)

        return parent