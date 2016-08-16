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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            if root.left is None:
                return self.minDepth(root.right) + 1
            if root.right is None:
                return self.minDepth(root.left) + 1

            left_min = self.minDepth(root.left)
            right_min = self.minDepth(root.right)
            return 1 + left_min if left_min < right_min else 1 + right_min
