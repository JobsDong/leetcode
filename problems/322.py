#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        nums = [-1] * (amount+1)
        for coin in coins:
            if coin <= amount:
                nums[coin] = 1

        for i in xrange(1, amount+1):
            if nums[i] == -1:
                min_num = -1
                for coin in coins:
                    if i-coin > 0 and nums[i-coin] != -1:
                        if min_num is -1 or nums[i-coin]+1 < min_num:
                            min_num = nums[i-coin]+1

                nums[i] = min_num

        return nums[amount]


if __name__ == "__main__":
    # print Solution().coinChange([1,2,5], 11)
    print Solution().coinChange([2], 1)