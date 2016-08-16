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

    def build_node(self, nums, i, n):
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(nums[i])
        else:
            mid = i+n/2-1 if n % 2 == 0 else (n-1)/2+i
            node = TreeNode(nums[mid])

            node.left = self.build_node(nums, i, mid-i)
            node.right = self.build_node(nums, mid+1, n-mid+i-1)
            return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        return self.build_node(nums, 0, len(nums))

if __name__ == "__main__":
    Solution().build_node([1,2,3,4], 0, 4)