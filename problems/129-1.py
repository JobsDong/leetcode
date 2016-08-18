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
            return [[0, r.val]]

        left_l = [] if r.left is None else self.path(r.left)
        right_l = [] if r.right is None else self.path(r.right)

        l = left_l + right_l
        for i in xrange(0, len(l)):
            l[i][0] += 1
            l[i][1] += r.val * (10**l[i][0])
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
        for count, item in l:
            total += item

        return total

def tree_nodes():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.right.left = TreeNode(4)
    return head


if __name__ == "__main__":
    print Solution().path(tree_nodes())