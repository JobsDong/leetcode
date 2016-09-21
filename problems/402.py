#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        min_num_list = []
        n = len(num)
        start = 0
        left_k = n - k

        while left_k > 0:

            min_num = num[start]
            min_i = start
            for i in xrange(start+1, n-left_k+1):
                if min_num > num[i]:
                    min_num = num[i]
                    min_i = i

            min_num_list.append(min_num)
            left_k -= 1
            start = min_i+1

        return "".join(min_num_list).lstrip('0') or "0"

if __name__ == "__main__":
    print Solution().removeKdigits("10", 2)