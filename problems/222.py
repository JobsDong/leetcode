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

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # depth
        end = 0
        depth = 0
        p = root
        while p.left:
            depth += 1
            end = (end << 1) + 1
            p = p.left
        depth += 1

        # binary search
        start = 0
        while start < end:
            mid = (start+end)/2
            if mid == start:
                break

            # weather mid node is exist ?
            p = root
            t = mid
            i = 0
            while p:
                if depth-2-i >= 0 and t >> (depth-2-i) & 1 == 1:
                    p = p.right
                else:
                    p = p.left
                i += 1

            if i == depth:
                start = mid
            else:
                end = mid

        # test final node
        p = root
        t = end
        i = 0
        while p:
            if depth-2-i >= 0 and t >> (depth-2-i) & 1 == 1:
                p = p.right
            else:
                p = p.left
            i += 1

        if i == depth:
            return 2 ** (depth-1) + end
        else:
            return 2 ** (depth-1) + start






