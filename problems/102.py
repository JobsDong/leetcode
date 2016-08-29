#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = [[]]

        que = deque()
        que.append(root)
        que.append(None)

        while len(que) != 0:
            node = que.popleft()
            if node is not None:
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                result[len(result)-1].append(node.val)
            else:
                if len(que) != 0:
                    que.append(None)
                    result.append([])

        return result
