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

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            stack = [root.right, root.val, root.left]

            result = []

            while len(stack) > 0:
                p = stack.pop()
                if p is not None:
                    if isinstance(p, int):
                        result.append(p)
                    else:
                        stack.append(p.right)
                        stack.append(p.val)
                        stack.append(p.left)
            return result
