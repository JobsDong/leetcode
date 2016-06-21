#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        i = n-1
        plus = 1

        while i >= 0:
            s = digits[i] + plus
            if s >= 10:
                digits[i] = s - 10
                plus = 1
            else:
                digits[i] = s
                plus = 0

            i -= 1

        if plus == 0:
            return digits
        else:
            return [1] + digits