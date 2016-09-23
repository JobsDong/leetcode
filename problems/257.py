#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        l = []

        def build_line(r, line):

            if r.left is None and r.right is None:
                l.append(line)
                return

            if r.left:
                build_line(r.left, "%s->%s" % (line, r.left.val))
            if r.right:
                build_line(r.right, "%s->%s" % (line, r.right.val))

        if root is None:
            return l

        build_line(root, "%s" % root.val)

        return l