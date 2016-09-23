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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []

        def right_side(r, i):
            if r is None:
                return

            if i >= len(l):
                l.append(r.val)

            if r.right:
                right_side(r.right, i+1)

            if r.left:
                right_side(r.left, i+1)

        right_side(root, 0)

        return l
