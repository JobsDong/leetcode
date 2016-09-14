#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        profits = [0]
        max_profits = [0]
        max_buys = [-prices[0]]

        for i in xrange(1, len(prices)):
            profits.append(max_buys[i-1]+prices[i])
            max_profits.append(max(max_profits[-1], profits[-1]))
            max_buys.append(max(max_buys[-1], max_profits[i-2]-prices[i]))

        return max_profits[-1]

if __name__ == "__main__":
    # print Solution().maxProfit([1, 2, 3, 0, 2])
    print Solution().maxProfit([1,4,2,7])