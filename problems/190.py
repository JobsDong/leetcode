#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        for i in xrange(0, 32):
            if (1 << i) & n == 0:
                pass
            else:
                m |= 0x80000000 >> i
        return m