#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x

        while start <= end:
            mid = (start + end)/2
            if mid * mid < x:
                start = mid+1
            elif mid * mid > x:
                end = mid-1
            else:
                return mid

        if end * end > x:
            return end-1
        else:
            return end


if __name__ == "__main__":
    print Solution().mySqrt(10)