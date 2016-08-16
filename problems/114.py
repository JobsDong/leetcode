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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        else:
            self.flatten(root.left)
            self.flatten(root.right)

            if root.left is None:
                return
            else:
                p = root.left
                while p.right:
                    p = p.right

                p.right = root.right

                root.right = root.left
                root.left = None
