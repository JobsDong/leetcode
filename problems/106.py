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

    def build_node(self, inorder, postorder, i, j, n):
        if n == 0:
            return None
        elif n == 1:
            node = TreeNode(inorder[i])
            return node
        else:
            r_v = postorder[j+n-1]
            r_i = inorder.index(r_v)
            node = TreeNode(r_v)
            node.left = self.build_node(inorder, postorder, i, j, r_i-i)
            node.right = self.build_node(inorder, postorder, r_i+1, j+r_i-i, n-r_i+i-1)
            return node

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build_node(inorder, postorder, 0, 0, len(inorder))


if __name__ == "__main__":
    Solution().build_node([1,3,2], [3,2,1], 0, 0, 3)