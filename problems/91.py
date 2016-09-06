#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        if s[0] == '0':
            l1 = 0
        else:
            l1 = 1

        if l1 == 0 or len(s) <= 1:
            return l1

        if s[1] == '0':
            if int(s[0:2]) > 26:
                l2 = 0
            else:
                l2 = 1
        else:
            if int(s[0:2]) > 26:
                l2 = 1
            else:
                l2 = 2

        for i in xrange(2, len(s)):
            l3 = 0
            if s[i] != '0':
                l3 += l2
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                l3 += l1

            if l3 == 0:
                return 0

            l1 = l2
            l2 = l3

        return l2


if __name__ == "__main__":
    print Solution().numDecodings("120328210")