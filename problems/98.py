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

    def max_node(self, r):
        p = r
        while p.right:
            p = p.right

        return p

    def min_node(self, r):
        p = r
        while p.left:
            p = p.left

        return p

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is not None:
            if self.max_node(root.left).val >= root.val:
                return False

        if not self.isValidBST(root.left):
            return False

        if root.right is not None:
            if self.min_node(root.right).val <= root.val:
                return False

        if not self.isValidBST(root.right):
            return False

        return True


def tree():
    r = TreeNode(2)
    r.left = TreeNode(1)
    r.right = TreeNode(3)
    return r


if __name__ == "__main__":
    print Solution().isValidBST(tree())
