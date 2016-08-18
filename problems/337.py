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

    def __init__(self):
        self.cache = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left not in self.cache:
            self.cache[root.left] = self.rob(root.left)
        if root.right not in self.cache:
            self.cache[root.right] = self.rob(root.right)
        r1 = self.cache[root.left] + self.cache[root.right]

        r2 = root.val
        if root.left is not None:
            if root.left.left not in self.cache:
                self.cache[root.left.left] = self.rob(root.left.left)
            if root.left.right not in self.cache:
                self.cache[root.left.right] = self.rob(root.left.right)

            r2 += self.cache[root.left.left] + self.cache[root.left.right]

        if root.right is not None:
            if root.right.left not in self.cache:
                self.cache[root.right.left] = self.rob(root.right.left)
            if root.right.right not in self.cache:
                self.cache[root.right.right] = self.rob(root.right.right)
            r2 += self.cache[root.right.left] + self.cache[root.right.right]

        return r1 if r1 > r2 else r2
