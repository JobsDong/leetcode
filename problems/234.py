#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        root = ListNode(0)
        root.next = None

        p = head

        # count
        i = 0
        while p:
            i += 1
            p = p.next

        n = i
        # reverse n/2
        p = head
        i = 0
        while p:
            if n % 2 == 0:
                if i >= n/2:
                    break
            else:
                if i >= n/2:
                    p = p.next
                    break
            i += 1
            temp = p.next
            p.next = root.next
            root.next = p
            p = temp

        #
        q = root.next
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next

        if p == q:
            return True
        else:
            return False

def linked_list(l):
    root = ListNode(0)
    root.next = None
    p = root

    for c in l:
        p.next = ListNode(c)
        p = p.next

    return root.next

if __name__ == "__main__":
    print Solution().isPalindrome(linked_list([]))