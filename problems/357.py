#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        z_f = [0, 1]
        p_f = [0, 9]
        total = 10

        for i in xrange(2, n+1):
            z_f.append(z_f[-1] * (10-i+1) + p_f[-2] * (10-i+1))
            p_f.append(p_f[-1] * (9-i+1))
            total += z_f[-1] + p_f[-1]

        return total

if __name__ == "__main__":
    print Solution().countNumbersWithUniqueDigits(3)