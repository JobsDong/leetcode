#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

# static dp


class Solution(object):

    l = [1, 1]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(len(self.l), n+1):
            j = 1
            min_count = i
            while j * j <= i:
                if j * j == i:
                    min_count = 1
                    break
                t = self.l[j*j] + self.l[i-j*j]
                min_count = min(min_count, t)
                j += 1
            self.l.append(min_count)

        return self.l[n]

if __name__ == "__main__":
    s = Solution()
    # s.numSquares(100)
    print s.numSquares(9975)
    # print s.numSquares(90000)