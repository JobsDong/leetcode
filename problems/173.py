#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        p = root
        while p:
            self.stack.append(p)
            if p.left is not None:
                p = p.left
            else:
                break

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        val = self.stack[len(self.stack)-1].val
        p = self.stack.pop().right

        while p:
            self.stack.append(p)
            if p.left is not None:
                p = p.left
            else:
                break
        return val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())