#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        count = 0
        if n & 1 == 1:
            count += 1

        while n > 0:
            n >>= 1
            if n & 1 == 1:
                count += 1
                if count >= 2:
                    return False
        return True

if __name__ == "__main__":
    print Solution().isPowerOfTwo(3)
