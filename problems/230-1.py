#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def count(self, r):
        if r is None:
            return 0
        else:
            return self.count(r.left) + self.count(r.right) + 1

    def search(self, r, k):
        c = self.count(r.left)
        if k == c+1:
            return r.val
        elif k < c+1:
            return self.search(r.left, k)
        else:
            return self.search(r.right, k-c-1)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.search(root, k)
