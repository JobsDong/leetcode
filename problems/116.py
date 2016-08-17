#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return

        queue = deque()
        queue.append(root)
        queue.append(None)

        while len(queue) > 0:
            p = queue.popleft()
            if p is None:
                if len(queue) > 0:
                    queue.append(None)
                else:
                    break
            else:
                if p.left is not None:
                    queue.append(p.left)
                if p.right is not None:
                    queue.append(p.right)

                p.next = queue[0]

