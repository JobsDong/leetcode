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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []

        def path_sum(root, sum, l):
            if root is None:
                return

            if root.left is None and root.right is None:
                if root.val == sum:
                    l.append(root.val)
                    paths.append(l)
                    return
                else:
                    return

            if root.left:
                new_l = list(l)
                new_l.append(root.val)
                path_sum(root.left, sum-root.val, new_l)

            if root.right:
                new_l = list(l)
                new_l.append(root.val)
                path_sum(root.right, sum-root.val, new_l)

        path_sum(root, sum, [])

        return paths