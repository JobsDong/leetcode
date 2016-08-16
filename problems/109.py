#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def build_node(self, r, n):
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(r.val)
        else:
            mid = n/2-1 if n % 2 == 0 else (n-1)/2

            p = r
            i = 0
            while i < mid:
                p = p.next
                i += 1

            node = TreeNode(p.val)
            node.left = self.build_node(r, mid)
            node.right = self.build_node(p.next, n-mid-1)
            return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        i = 0
        while p:
            i += 1
            p = p.next

        return self.build_node(head, i)


if __name__ == "__main__":
    Solution().build_node()