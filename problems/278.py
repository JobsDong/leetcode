#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(v):
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n

        while start < end:

            if start+1 == end:
                if isBadVersion(start):
                    return start
                else:
                    return end

            mid = (start+end)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid

        return start
