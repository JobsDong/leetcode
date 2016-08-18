#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

    def path(self, r):
        if r.left is None and r.right is None:
            return [[r.val]]

        left_l = [] if r.left is None else self.path(r.left)
        right_l = [] if r.right is None else self.path(r.right)

        l = left_l + right_l
        for i in xrange(0, len(l)):
            l[i].append(r.val)
        return l

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.path(root)

        total = 0
        for item in l:
            for i, num in enumerate(item):
                total += num * (10 ** i)

        return total
