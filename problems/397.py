#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        j = 0

        while n > 1:

            if n % 2 == 0:
                n >>= 1
                j += 1
            else:
                if n == 3:
                    j += 1
                    n -= 1
                else:
                    if (n+1) % 4 == 0:
                        j += 1
                        n += 1
                    else:
                        j += 1
                        n -= 1
        return j

if __name__ == "__main__":
    print Solution().integerReplacement(11111111)