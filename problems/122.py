#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if n <= 1:
            return 0
        max_buy = -prices[0]
        max_total = 0

        for i in xrange(1, n):
            t = max_total - prices[i]
            max_total = max(max_buy+prices[i], max_total)
            max_buy = max(max_buy, t)
        return max_total


if __name__ == "__main__":
    print Solution().maxProfit([2,3])