#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):

    def is_additive(self, num, i, j):
        start = j
        end = j+1

        a1 = int(num[0:i])
        a2 = int(num[i:j])

        while start <len(num) and end <= len(num):
            if num[start:start+1] == "0" and end > start+1:
                return False

            if a1 + a2 == int(num[start:end]):
                a1 = a2
                a2 = int(num[start:end])
                start = end
                end += 1
            else:
                end += 1

        if start > len(num)-1:
            return True
        else:
            return False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        for i in xrange(1, n-1):
            if num[0:1] == '0' and i > 1:
                return False

            for j in xrange(i+1, n):
                if num[i:i+1] == '0' and j > i+1:
                    break
                else:
                    if self.is_additive(num, i, j):
                        return True
        return False


if __name__ == '__main__':
    # print Solution().isAdditiveNumber("112358")
    # print Solution().isAdditiveNumber("199100199")
    # print Solution().isAdditiveNumber("1203")
    print Solution().isAdditiveNumber("0235813")