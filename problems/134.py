#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        n = len(gas)

        last_start = n-1
        last_end = n-1
        last_gas = 0

        for i in xrange(n-1, -1, -1):
            left_gas = sum(gas[i:last_start]) - sum(cost[i:last_start])
            if left_gas >= 0:
                last_start = i
                last_gas += left_gas

                while last_end <= n-1:
                    if last_gas + gas[last_end] >= cost[last_end]:
                        last_gas += gas[last_end] - cost[last_end]
                        last_end = (last_end + 1) % n

                        if last_end == n-1:
                            return last_start
                    else:
                        break

        return -1

if __name__ == "__main__":
    print Solution().canCompleteCircuit([1, 4], [2, 3])