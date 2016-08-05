#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while True:

            total = 0
            while n != 0:
                total += (n % 10) * (n % 10)
                n /= 10

            if total == 1:
                return True
            if total in s:
                return False
            else:
                s.add(total)

            n = total

        return False




if __name__ == "__main__":
    print Solution().isHappy(68)