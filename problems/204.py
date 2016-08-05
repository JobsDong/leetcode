#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = []
        for i in xrange(0, n):
            c.append(True)

        if len(c) >= 1:
            c[0] = False
        if len(c) >= 2:
            c[1] = False

        j = 2
        while j * j < n:
            if c[j]:
                k = 2
                while j * k < n:
                    c[j*k] = False
                    k += 1
            j += 1

        count = 0
        for m in xrange(2, n):
            if c[m]:
                count += 1

        return count

if __name__ == "__main__":
    print Solution().countPrimes(1500000)