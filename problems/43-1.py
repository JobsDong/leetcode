#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1)
        m = len(num2)
        result = [0] * (n + m)

        i = 0
        while i < m:

            plus = 0
            j = 0
            while j < n:
                t = (result[i+j] + plus + int(num1[n-j-1]) * int(num2[m-i-1])) % 10
                plus = (result[i+j] + plus + int(num1[n-j-1]) * int(num2[m-i-1])) / 10
                result[i+j] = t

                j += 1

            if plus > 0:
                result[i+j] = plus
            i += 1

        final_total = []
        not_add = False
        for i in xrange(len(result)-1, -1, -1):
            if i == len(result)-1 and result[i] == 0:
                not_add = True

            if result[i] != 0:
                not_add = False

            if not not_add:
                final_total.append(str(result[i]))

        if len(final_total) == 0:
            return "0"
        else:
            return "".join(final_total)

if __name__ == "__main__":
    print Solution().multiply("9", "9")
