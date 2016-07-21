#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def compare(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if left.val != right.val:
                return False
            else:
                return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        elif root.left is not None and root.right is not None:
            return self.compare(root.left, root.right)
        else:
            return False


if __name__ == "__main__":
    print [2, 3, None, 2, None, 3]