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

    def build_node(self, preorder, inorder, i, j, n):
        if n == 0:
            return None
        elif n == 1:
            t = TreeNode(preorder[i])
            return t
        else:
            r_v = preorder[i]
            r_i = inorder.index(r_v)

            r = TreeNode(r_v)
            r.left = self.build_node(preorder, inorder, i+1, j, r_i-j)
            r.right = self.build_node(preorder, inorder, i+r_i-j+1, r_i+1, n-(r_i-j+1))
            return r

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build_node(preorder, inorder, 0, 0, len(preorder))