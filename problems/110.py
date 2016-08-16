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

    def depth(self, r):
        if r is None:
            return 0
        else:
            l_d = self.depth(r.left)
            r_d = self.depth(r.right)
            return l_d + 1 if l_d > r_d else r_d + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_dep = self.depth(root.left)
        right_dep = self.depth(root.right)
        if -1 <= left_dep - right_dep <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
