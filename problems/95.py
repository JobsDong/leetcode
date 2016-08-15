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


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []

        def generate(begin, end):
            if begin > end:
                return [None]
            elif begin == end:
                node = TreeNode(begin)
                return [node]
            else:
                nodes = []
                for i in xrange(begin, end+1):
                    left_nodes = generate(begin, i-1)
                    right_nodes = generate(i+1, end)

                    for left_node in left_nodes:
                        for right_node in right_nodes:
                            r = TreeNode(i)
                            r.left = left_node
                            r.right = right_node
                            nodes.append(r)

                return nodes

        return generate(1, n)
