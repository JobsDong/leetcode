#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        max_l = max(n, m)

        sum_l = ["0"] * max_l

        i = 1
        plus = 0
        while i <= max_l:
            n1 = int(a[n-i]) if n >=i else 0
            n2 = int(b[m-i]) if m >= i else 0

            sum_l[max_l-i] = str((n1 + n2 + plus) % 2)
            plus = (n1 + n2 + plus) / 2
            i += 1
        if plus > 0:
            return str(plus) + "".join(sum_l)
        else:
            return "".join(sum_l)





if __name__ == "__main__":
    print Solution().addBinary("111", "101")