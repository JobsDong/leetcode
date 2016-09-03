#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        l1 = 1
        l2 = 2

        for i in xrange(3, n+1):
            t = l2
            l2 = l1 + t
            l1 = t

        return l2
