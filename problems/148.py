#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def merge(self,r1, r2):
        p = r1
        q = r2

        while p.next and q.next:

            if p.next.val < q.next.val:
                p = p.next
            else:
                t1 = q.next
                q.next = q.next.next
                t1.next = p.next
                p.next = t1
                p = p.next

        if p.next is None:
            p.next = q.next

    def merge_sort(self, r, n):
        if n <= 1:
            return

        p = r
        i = 0
        while p.next and i < n/2:
            i += 1
            p = p.next

        r2 = ListNode("text")
        r2.next = p.next
        p.next = None
        self.merge_sort(r, i)
        self.merge_sort(r2, n-i)
        self.merge(r, r2)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode("text")
        root.next = head

        p = root
        i = 0
        while p.next:
            i += 1
            p = p.next

        self.merge_sort(root, i)

        return root.next

def linked_list(l):
    root = ListNode("text")
    p = root

    for i in l:
        p.next = ListNode(i)
        p = p.next
    return root.next

def print_list2(r):
    p = r
    l = []
    while p:
        l.append(p.val)
        p = p.next

    return l

if __name__ == "__main__":
    r = linked_list([1, 3, 2, 5, 4])
    Solution().sortList(r)
    print print_list2(r)






