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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s_p = root
        s_q = root

        while True:
            if p.val > s_p.val:
                s_p = s_p.right
            elif p.val < s_p.val:
                s_p = s_p.left
            else:
                pass

            last = s_q

            if q.val > s_q.val:
                s_q = s_q.right
            elif q.val < s_q.val:
                s_q = s_q.left
            else:
                pass

            if s_q != s_p:
                return last
