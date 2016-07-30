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

    def _pre_order(self, r, l):
        if r is not None:
            l.append(r.val)
            self._pre_order(r.left, l)
            self._pre_order(r.right, l)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self._pre_order(root, l)
        return l



if __name__ == "__main__":
    print Solution().preorderTraversal()