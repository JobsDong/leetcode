#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num

        while start <= end:
            mid = (start+end)/2

            if start+1 == end:
                if end * end == num or start * start == num:
                    return True
                else:
                    return False

            if mid * mid > num:
                end = mid
            elif mid * mid < num:
                start = mid
            else:
                return True

        if start * start == num:
            return True
        else:
            return False

if __name__ == "__main__":
    print Solution().isPerfectSquare(2)