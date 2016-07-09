#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def __init__(self):
        self.cache = ["1"]

    def get_next_num(self, num):
        next_num = ""
        i = 0
        begin = None

        for c in num:
            if begin is None:
                begin = c
                i += 1
            else:
                if c == begin:
                    i += 1
                else:
                    next_num += "%d%s" % (i, begin)
                    i = 1
                    begin = c

        next_num += "%d%s" % (i, begin)
        return next_num


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if len(self.cache) < n:
            for i in xrange(len(self.cache), n):
                self.cache.append(self.get_next_num(self.cache[i-1]))

        return self.cache[n-1]


if __name__ == "__main__":
    print Solution().countAndSay(5)