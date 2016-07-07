#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 1:
            return s

        matrix = [[] for i in xrange(0, numRows)]

        i = 0
        k = 0
        plus = True

        while True:
            if not plus and (i == 0 or i == numRows-1):
                c = '#'
            else:
                c = s[k]
                k += 1

            matrix[i].append(c)

            if k == len(s):
                break

            if plus:
                if i == numRows-1:
                    plus = False
                else:
                    i += 1
            else:
                if i == 0:
                    plus = True
                else:
                    i -= 1

        str_list = []
        for i in xrange(0, len(matrix)):
            for c in matrix[i]:
                if c != '#':
                    str_list.append(c)
        return "".join(str_list)


if __name__ == "__main__":
    print Solution().convert("", 3)