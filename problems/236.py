#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class TreeNode(object):

    def __init__(self, v):
        self.val = v
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
        if root is None or root is p or root is q:
            return root

        left_common = self.lowestCommonAncestor(root.left, p, q)
        right_common = self.lowestCommonAncestor(root.right, p, q)

        if left_common is None and right_common is None:
            return None
        elif left_common is None and right_common is not None:
            return right_common
        elif left_common is not None and right_common is None:
            return left_common
        else:
            if left_common != right_common:
                return root
            else:
                return right_common


if __name__ == "__main__":
    r = TreeNode(-1)
    r.left = TreeNode(0)
    r.left.left = TreeNode(-2)
    r.left.left.left = TreeNode(8)
    r.left.right = TreeNode(4)
    r.right = TreeNode(3)

    print Solution().lowestCommonAncestor(r, r.left.left.left, r.left.right).val