#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_num = 0
        max_profit = 0

        for i in xrange(len(prices)-1, -1, -1):
            profit = max_num - prices[i]
            if profit > max_profit:
                max_profit = profit
            if prices[i] > max_num:
                max_num = prices[i]

        return max_profit


if __name__ == "__main__":
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])