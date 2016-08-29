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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = [[]]
        i = 0

        stack1 = list()
        stack1.append(root)
        stack = list()

        while len(stack1) != 0 or len(stack) != 0:

            if i % 2 == 0:
                node = stack1.pop()
            else:
                node = stack.pop()

            result[i].append(node.val)
            if i % 2 == 0:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

                if len(stack1) == 0 and len(stack) != 0:
                    i += 1
                    result.append([])
            else:
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)

                if len(stack) == 0 and len(stack1) != 0:
                    i += 1
                    result.append([])

        return result


def tree():
    r = TreeNode(3)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)
    return r

if __name__ == "__main__":
    print Solution().zigzagLevelOrder(tree())