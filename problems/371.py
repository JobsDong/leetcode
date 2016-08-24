#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 1
        p = 0
        result = 0

        while x <= 0x80000000:
            a1 = x & a
            b1 = x & b

            # plus with p
            if p == 0:
                if a1 | b1 == 0:
                    r1 = 0
                elif a1 & b1 == 0:
                    r1 = 1
                else:
                    r1 = 0
                    p = 1
            else:
                if a1 | b1 == 0:
                    p = 0
                    r1 = 1
                elif a1 & b1 == 0:
                    r1 = 0
                    p = 1
                else:
                    r1 = 1
                    p = 1

            if r1 == 1:
                result |= x

            x <<= 1

        if result & 0x8000000 == 0:
            return result
        else:
            return ~(result ^ 0xFFFFFFFF)

if __name__ == "__main__":
    print Solution().getSum(-2, -3)